#!/usr/bin/env python3
"""Synchronize core/micro-rule.md across platform adapters and validate cells-alive invariants."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

PRUNED_DIRS = {".git", "node_modules", "__pycache__"}
BINARY_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico"}

ROOT = Path(__file__).resolve().parent.parent
CORE_PATH = ROOT / "core" / "micro-rule.md"

MD_BEGIN = "<!-- BEGIN CELLS-ALIVE CORE -->"
MD_END = "<!-- END CELLS-ALIVE CORE -->"
TXT_BEGIN = "=== BEGIN CELLS-ALIVE CORE ==="
TXT_END = "=== END CELLS-ALIVE CORE ==="

MD_ADAPTERS = [
    ROOT / "rules" / "AGENTS.md",
    ROOT / "output-styles" / "cells-alive.md",
    ROOT / "adapters" / "agents-md-snippet.md",
    ROOT / "adapters" / "soul-md-snippet.md",
    ROOT / "adapters" / "cursor-rule.mdc",
]
TXT_ADAPTER = ROOT / "adapters" / "web-custom-instructions.txt"

ALLOWED_ANTIGRAVITY_PLUGIN_KEYS = {
    "name",
    "displayName",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "logo",
    "disabled",
    "suggestedPrompts",
}

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTBD\b"),
    re.compile(r"\bTODO\b"),
    re.compile(r"\bFIXME\b"),
    re.compile(r"<your-", re.IGNORECASE),
]

EXTERNAL_ASSET_RE = re.compile(
    r"""(?:<(?:img|script|link|iframe|object|embed)\b[^>]*(?:src|href)\s*=\s*["']\s*(?:https?:|file:|//))|"""
    r"""(?:url\(\s*["']?\s*(?:https?:|file:|//))|"""
    r"""(?:@import\s+(?:url\()?\s*["']?\s*(?:https?:|file:|//))|"""
    r"""(?:fetch\(\s*["']\s*(?:https?:|file:|//))""",
    re.IGNORECASE,
)

SVG_ALLOWED_XMLNS_RE = re.compile(
    r"""xmlns(?::(?:svg|xlink))?\s*=\s*["']http://www\.w3\.org/(?:2000/svg|1999/xlink)["']""",
    re.IGNORECASE,
)

SVG_FORBIDDEN_RE = re.compile(
    r"(?:https?://|file://|<script\b|<foreignObject\b|\bon[a-z]+\s*=)",
    re.IGNORECASE,
)

LEGACY_TOKENS = (
    "-".join(["lab", "peer"]),
    "-".join(["LAB", "PEER"]),
    " ".join(["Lab", "Peer"]),
)


def read_utf8_no_bom(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"UTF-8 BOM detected in {path.relative_to(ROOT)}")
    return raw.decode("utf-8").replace("\r\n", "\n")


def write_utf8_lf(path: Path, text: str) -> None:
    normalized = text.replace("\r\n", "\n").rstrip("\n") + "\n"
    path.write_bytes(normalized.encode("utf-8"))


def strip_markdown_to_plain(md_text: str) -> str:
    lines: list[str] = []
    for raw_line in md_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        lines.append(line)
    return "\n".join(lines)


def replace_block(content: str, begin: str, end: str, payload: str, path: Path) -> str:
    pattern = re.compile(
        re.escape(begin) + r"\n.*?\n" + re.escape(end),
        re.DOTALL,
    )
    if not pattern.search(content):
        raise ValueError(f"Missing sync markers {begin!r} .. {end!r} in {path.relative_to(ROOT)}")
    replacement = f"{begin}\n{payload.strip()}\n{end}"
    return pattern.sub(lambda _m: replacement, content, count=1)


def extract_block(content: str, begin: str, end: str, path: Path) -> str:
    match = re.search(
        re.escape(begin) + r"\n(.*?)\n" + re.escape(end),
        content,
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"Missing sync markers in {path.relative_to(ROOT)}")
    return match.group(1)


def parse_frontmatter(md_text: str) -> tuple[dict[str, object], str]:
    if not md_text.startswith("---\n"):
        raise ValueError("Missing YAML frontmatter opening delimiter '---'")
    end_idx = md_text.find("\n---\n", 4)
    if end_idx == -1:
        raise ValueError("Missing YAML frontmatter closing delimiter '---'")
    fm_block = md_text[4:end_idx]
    body = md_text[end_idx + 5 :]
    data: dict[str, object] = {}
    lines = fm_block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith(" ") or line.lstrip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            raise ValueError(f"Malformed YAML frontmatter line: {line!r}")
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val in (">-", ">", "|", "|-"):
            folded: list[str] = []
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                folded.append(lines[i].strip())
                i += 1
            data[key] = " ".join(part for part in folded if part)
            continue
        data[key] = val.strip("\"'")
        i += 1
    return data, body


def do_sync() -> int:
    core_text = read_utf8_no_bom(CORE_PATH).strip()
    plain_text = strip_markdown_to_plain(core_text)

    for path in MD_ADAPTERS:
        current = read_utf8_no_bom(path)
        updated = replace_block(current, MD_BEGIN, MD_END, core_text, path)
        write_utf8_lf(path, updated)
        print(f"SYNCED: {path.relative_to(ROOT)}")

    txt_current = read_utf8_no_bom(TXT_ADAPTER)
    txt_updated = replace_block(txt_current, TXT_BEGIN, TXT_END, plain_text, TXT_ADAPTER)
    write_utf8_lf(TXT_ADAPTER, txt_updated)
    print(f"SYNCED: {TXT_ADAPTER.relative_to(ROOT)}")
    return 0


def do_check() -> int:
    failures: list[str] = []
    passes: list[str] = []

    def fail(msg: str) -> None:
        failures.append(msg)

    def ok(msg: str) -> None:
        passes.append(msg)

    # 1. Core budget check
    if not CORE_PATH.is_file():
        fail("Check 1: core/micro-rule.md does not exist")
        core_text = ""
        plain_text = ""
    else:
        core_text = read_utf8_no_bom(CORE_PATH).strip()
        non_empty_lines = [ln for ln in core_text.splitlines() if ln.strip()]
        byte_len = len(core_text.encode("utf-8"))
        if len(non_empty_lines) > 35:
            fail(f"Check 1: core/micro-rule.md non-empty lines = {len(non_empty_lines)} > 35")
        elif byte_len > 2000:
            fail(f"Check 1: core/micro-rule.md UTF-8 bytes = {byte_len} > 2000")
        else:
            ok(
                f"Check 1 PASS: core/micro-rule.md = {len(non_empty_lines)} non-empty lines, "
                f"{byte_len} UTF-8 bytes (<= 35 lines, <= 2000 bytes)"
            )
        plain_text = strip_markdown_to_plain(core_text)

    # 2. Adapter sync parity check
    drift_items: list[str] = []
    for path in MD_ADAPTERS:
        if not path.is_file():
            drift_items.append(f"missing {path.relative_to(ROOT)}")
            continue
        content = read_utf8_no_bom(path)
        expected = replace_block(content, MD_BEGIN, MD_END, core_text, path).rstrip("\n") + "\n"
        if content != expected:
            drift_items.append(f"drift in {path.relative_to(ROOT)}")
    if not TXT_ADAPTER.is_file():
        drift_items.append(f"missing {TXT_ADAPTER.relative_to(ROOT)}")
    else:
        txt_content = read_utf8_no_bom(TXT_ADAPTER)
        txt_expected = replace_block(txt_content, TXT_BEGIN, TXT_END, plain_text, TXT_ADAPTER).rstrip("\n") + "\n"
        if txt_content != txt_expected:
            drift_items.append(f"drift in {TXT_ADAPTER.relative_to(ROOT)}")
    if drift_items:
        fail("Check 2: adapter sync mismatch -> " + "; ".join(drift_items))
    else:
        ok(f"Check 2 PASS: all {len(MD_ADAPTERS) + 1} adapters match core/micro-rule.md with zero drift")

    # 3. rules/AGENTS.md must NOT have YAML frontmatter
    agents_rule_path = ROOT / "rules" / "AGENTS.md"
    if not agents_rule_path.is_file():
        fail("Check 3: rules/AGENTS.md missing")
    else:
        agents_rule = read_utf8_no_bom(agents_rule_path)
        if agents_rule.lstrip().startswith("---"):
            fail("Check 3: rules/AGENTS.md must NOT start with YAML frontmatter '---'")
        else:
            ok("Check 3 PASS: rules/AGENTS.md is plain Markdown without YAML frontmatter")

    # 4. Web custom instructions char count <= 1500
    if TXT_ADAPTER.is_file():
        stripped_body = extract_block(read_utf8_no_bom(TXT_ADAPTER), TXT_BEGIN, TXT_END, TXT_ADAPTER)
        char_len = len(stripped_body)
        if char_len > 1500:
            fail(f"Check 4: adapters/web-custom-instructions.txt stripped body = {char_len} chars > 1500")
        else:
            ok(f"Check 4 PASS: web-custom-instructions.txt stripped body = {char_len} chars (<= 1500)")

    # 5. Root Antigravity plugin.json schema
    ag_manifest_path = ROOT / "plugin.json"
    if not ag_manifest_path.is_file():
        fail("Check 5: plugin.json missing")
    else:
        try:
            ag = json.loads(read_utf8_no_bom(ag_manifest_path))
            unknown_keys = set(ag.keys()) - ALLOWED_ANTIGRAVITY_PLUGIN_KEYS
            prompts = ag.get("suggestedPrompts", [])
            logo_rel = ag.get("logo", "")
            logo_exists = bool(logo_rel) and (ROOT / logo_rel).is_file()
            if unknown_keys:
                fail(f"Check 5: plugin.json has disallowed top-level keys: {sorted(unknown_keys)}")
            elif ag.get("name") != "cells-alive":
                fail(f"Check 5: plugin.json name is {ag.get('name')!r}, expected 'cells-alive'")
            elif not isinstance(prompts, list) or len(prompts) > 3:
                fail("Check 5: plugin.json suggestedPrompts invalid or > 3 items")
            elif not logo_exists:
                fail(f"Check 5: plugin.json logo {logo_rel!r} does not exist locally")
            else:
                ok(
                    f"Check 5 PASS: plugin.json schema valid (name='cells-alive', "
                    f"{len(prompts)} prompts, logo={logo_rel})"
                )
        except Exception as exc:
            fail(f"Check 5: plugin.json parse error: {exc}")

    # 6. .claude-plugin/plugin.json
    cc_manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not cc_manifest_path.is_file():
        fail("Check 6: .claude-plugin/plugin.json missing")
    else:
        try:
            cc = json.loads(read_utf8_no_bom(cc_manifest_path))
            if cc.get("name") != "cells-alive":
                fail(f"Check 6: .claude-plugin/plugin.json name is {cc.get('name')!r}, expected 'cells-alive'")
            else:
                ok("Check 6 PASS: .claude-plugin/plugin.json valid (name='cells-alive')")
        except Exception as exc:
            fail(f"Check 6: .claude-plugin/plugin.json parse error: {exc}")

    # 7. SKILL.md frontmatter + relative markdown links
    skill_path = ROOT / "skills" / "cells-alive" / "SKILL.md"
    if not skill_path.is_file():
        fail("Check 7: skills/cells-alive/SKILL.md missing")
    else:
        try:
            skill_text = read_utf8_no_bom(skill_path)
            fm, body = parse_frontmatter(skill_text)
            if fm.get("name") != "cells-alive" or not str(fm.get("description", "")).strip():
                fail("Check 7: SKILL.md frontmatter missing valid name/description")
            else:
                rel_links = re.findall(r"\]\(((?:\./|\.\./)[^)]+\.md)\)", body)
                missing_links = [
                    rel for rel in rel_links if not (skill_path.parent / rel).resolve().is_file()
                ]
                if not rel_links:
                    fail("Check 7: SKILL.md has no relative markdown links")
                elif missing_links:
                    fail(f"Check 7: SKILL.md broken relative links: {missing_links}")
                else:
                    ok(f"Check 7 PASS: SKILL.md frontmatter valid and {len(rel_links)} relative links resolve cleanly")
        except Exception as exc:
            fail(f"Check 7: SKILL.md validation error: {exc}")

    # 8. Offline self-contained HTML check
    html_path = ROOT / "examples" / "04-internal-summary-note.html"
    if not html_path.is_file():
        fail("Check 8: examples/04-internal-summary-note.html missing")
    else:
        html_text = read_utf8_no_bom(html_path)
        ext_hits = EXTERNAL_ASSET_RE.findall(html_text)
        if ext_hits:
            fail(f"Check 8: external asset/network dependencies detected in HTML: {ext_hits}")
        else:
            ok("Check 8 PASS: examples/04-internal-summary-note.html has zero external display/script dependencies")

    # 9. Repository-wide placeholder & BOM scan
    scan_targets = [
        ROOT / "plugin.json",
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github",
        ROOT / "core",
        ROOT / "rules",
        ROOT / "output-styles",
        ROOT / "skills",
        ROOT / "adapters",
        ROOT / "templates",
        ROOT / "examples",
        ROOT / "community",
        ROOT / "docs",
        ROOT / "locale",
        ROOT / "tests",
    ]
    files_to_scan: list[Path] = []
    for target in scan_targets:
        if target.is_file():
            if target.suffix.lower() not in BINARY_EXTS:
                files_to_scan.append(target)
        elif target.is_dir():
            for cur_dir, dirs, names in os.walk(target):
                dirs[:] = sorted(d for d in dirs if d not in PRUNED_DIRS)
                for fname in sorted(names):
                    fp = Path(cur_dir, fname)
                    if fp.suffix.lower() not in BINARY_EXTS:
                        files_to_scan.append(fp)

    placeholder_hits: list[str] = []
    for fpath in files_to_scan:
        try:
            text = read_utf8_no_bom(fpath)
        except Exception as exc:
            placeholder_hits.append(f"{fpath.relative_to(ROOT)} ({exc})")
            continue
        for pat in PLACEHOLDER_PATTERNS:
            m = pat.search(text)
            if m:
                placeholder_hits.append(f"{fpath.relative_to(ROOT)} matched {m.group(0)!r}")
    if placeholder_hits:
        fail("Check 9: unresolved placeholders or encoding issues -> " + "; ".join(placeholder_hits))
    else:
        ok(f"Check 9 PASS: scanned {len(files_to_scan)} files with zero placeholders and zero UTF-8 BOMs")

    # 10. Community co-creation files & SVG safety check
    required_community_files = [
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "01-submit-moment.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "02-submit-meme-or-sticker.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "03-tone-calibration.yml",
        ROOT / "community" / "README.md",
        ROOT / "community" / "moments-low.md",
        ROOT / "community" / "moments-high.md",
        ROOT / "community" / "memes-and-lines.md",
        ROOT / "community" / "stickers" / "README.md",
    ]
    missing_community = [str(p.relative_to(ROOT)) for p in required_community_files if not p.is_file()]
    sticker_svgs = sorted((ROOT / "community" / "stickers").glob("*.svg")) if (ROOT / "community" / "stickers").is_dir() else []
    root_icon = ROOT / "icon.svg"
    if not root_icon.is_file():
        missing_community.append("icon.svg")
    all_svgs = ([root_icon] if root_icon.is_file() else []) + sticker_svgs
    svg_issues: list[str] = []
    if not sticker_svgs:
        svg_issues.append("no *.svg files under community/stickers/")
    for svg_path in all_svgs:
        raw_bytes = svg_path.read_bytes()
        if len(raw_bytes) > 8192:
            svg_issues.append(f"{svg_path.relative_to(ROOT)} size={len(raw_bytes)} > 8192 bytes")
        svg_text = read_utf8_no_bom(svg_path)
        svg_without_std_xmlns = SVG_ALLOWED_XMLNS_RE.sub("", svg_text)
        bad = SVG_FORBIDDEN_RE.search(svg_without_std_xmlns)
        if bad:
            svg_issues.append(f"{svg_path.relative_to(ROOT)} forbidden construct {bad.group(0)!r}")
    if missing_community or svg_issues:
        details = ([] if not missing_community else [f"missing: {missing_community}"]) + svg_issues
        fail("Check 10: community/SVG check failed -> " + "; ".join(details))
    else:
        ok(
            f"Check 10 PASS: community scaffolding complete and all {len(all_svgs)} SVGs "
            "are <= 8192 bytes with zero scripts/external links"
        )

    # 11. Zero legacy rename drift across entire repository
    legacy_hits: list[str] = []
    all_repo_files: list[Path] = []
    for cur_dir, dirs, names in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in PRUNED_DIRS)
        for fname in sorted(names):
            fp = Path(cur_dir, fname)
            if fp.suffix.lower() not in BINARY_EXTS:
                all_repo_files.append(fp)
    for fpath in all_repo_files:
        text = read_utf8_no_bom(fpath)
        for tok in LEGACY_TOKENS:
            if tok in text:
                legacy_hits.append(f"{fpath.relative_to(ROOT)} contains {tok!r}")
    if legacy_hits:
        fail("Check 11: legacy brand string detected -> " + "; ".join(legacy_hits))
    else:
        ok(f"Check 11 PASS: scanned all {len(all_repo_files)} repo files with zero legacy name drift")

    for line in passes:
        print(line)
    if failures:
        for line in failures:
            print(f"FAIL: {line}", file=sys.stderr)
        return 1
    print("ALL 11 CHECKS PASSED.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync and validate cells-alive adapters and manifests.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--sync", action="store_true", help="Sync core/micro-rule.md to all platform adapters.")
    group.add_argument("--check", action="store_true", help="Run all 11 integrity, budget, community, and schema checks.")
    args = parser.parse_args()
    if args.sync:
        return do_sync()
    return do_check()


if __name__ == "__main__":
    raise SystemExit(main())
