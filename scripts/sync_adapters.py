#!/usr/bin/env python3
"""Synchronize core/micro-rule.md across platform adapters and validate cells-alive invariants."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

PRUNED_DIRS = {".git", "node_modules", "__pycache__"}
BINARY_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".tgz", ".zip", ".pdf", ".docx", ".whl"}

ROOT = Path(__file__).resolve().parent.parent
CORE_PATH = ROOT / "core" / "micro-rule.md"

MD_BEGIN = "<!-- BEGIN CELLS-ALIVE CORE -->"
MD_END = "<!-- END CELLS-ALIVE CORE -->"
TXT_BEGIN = "=== BEGIN CELLS-ALIVE CORE ==="
TXT_END = "=== END CELLS-ALIVE CORE ==="
HTML_BEGIN = '<script type="text/plain" id="rules">'
HTML_END = "</script>"

MD_ADAPTERS = [
    ROOT / "rules" / "AGENTS.md",
    ROOT / "output-styles" / "cells-alive.md",
    ROOT / "adapters" / "agents-md-snippet.md",
    ROOT / "adapters" / "soul-md-snippet.md",
    ROOT / "adapters" / "cursor-rule.mdc",
]
TXT_ADAPTER = ROOT / "adapters" / "web-custom-instructions.txt"
HTML_ADAPTER = ROOT / "adapters" / "start.html"

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
    r"""(?:<(?:img|script|link|iframe|object|embed|video|audio|source|track|form)\b[^>]*(?:src|href|action|poster|srcset|ping)\s*=\s*(?:["']?\s*(?:https?:|file:|//|javascript:|ftp:)|["']\s*(?!#)\S))|"""
    r"""(?:<link\b[^>]*\brel\s*=\s*["']?stylesheet\b)|"""
    r"""(?:<base\b[^>]*\bhref\s*=)|"""
    r"""(?:\burl\(\s*["']?\s*(?:https?:|file:|//|data:))|"""
    r"""(?:@import\s+(?:url\()?\s*["']?\s*(?:https?:|file:|//))|"""
    r"""(?:\b(?:fetch|XMLHttpRequest|WebSocket|EventSource)\b|\bnavigator\.sendBeacon\b|\bimport\s*\(|\bdocument\.cookie\b|\bindexedDB\b)""",
    re.IGNORECASE,
)

SVG_ALLOWED_XMLNS_RE = re.compile(
    r"""xmlns(?::(?:svg|xlink))?\s*=\s*["']http://www\.w3\.org/(?:2000/svg|1999/xlink)["']""",
    re.IGNORECASE,
)

SVG_FORBIDDEN_RE = re.compile(
    r"(?:https?://|file://|//|javascript:|ftp:|data:image/|@import\b|url\(\s*['\"]?\s*//|<script\b|<foreignObject\b|\bon[a-z]+\s*=)",
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
    raw = normalized.encode("utf-8")
    tmp_path: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            tmp_path = handle.name
            handle.write(raw)
        os.replace(tmp_path, path)
    finally:
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass


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


def _validate_core_payload(core_text: str, plain_text: str) -> None:
    non_empty_lines = [ln for ln in core_text.splitlines() if ln.strip()]
    byte_len = len(core_text.encode("utf-8"))
    if len(non_empty_lines) > 35:
        raise ValueError(f"core/micro-rule.md non-empty lines = {len(non_empty_lines)} > 35")
    if byte_len > 2000:
        raise ValueError(f"core/micro-rule.md UTF-8 bytes = {byte_len} > 2000")
    if len(plain_text) > 1500:
        raise ValueError(f"stripped core rule = {len(plain_text)} chars > 1500")
    for token in (MD_BEGIN, MD_END):
        if token in core_text:
            raise ValueError(f"core payload contains sync delimiter {token!r}")
    for token in (TXT_BEGIN, TXT_END, HTML_BEGIN):
        if token in plain_text:
            raise ValueError(f"plain payload contains sync delimiter {token!r}")
    if re.search(r"</script\s*>", plain_text, re.IGNORECASE):
        raise ValueError("plain payload contains closing '</script>' HTML breakout sequence")


def replace_block(content: str, begin: str, end: str, payload: str, path: Path) -> str:
    begin_count = content.count(begin)
    if begin_count != 1:
        raise ValueError(f"Expected exactly 1 {begin!r} marker in {path.relative_to(ROOT)}, found {begin_count}")
    pattern = re.compile(
        re.escape(begin) + r"\n.*?\n" + re.escape(end),
        re.DOTALL,
    )
    matches = pattern.findall(content)
    if len(matches) != 1:
        raise ValueError(f"Missing or duplicate sync block {begin!r} .. {end!r} in {path.relative_to(ROOT)}")
    replacement = f"{begin}\n{payload.strip()}\n{end}"
    return pattern.sub(lambda _m: replacement, content, count=1)


def extract_block(content: str, begin: str, end: str, path: Path) -> str:
    begin_count = content.count(begin)
    if begin_count != 1:
        raise ValueError(f"Expected exactly 1 {begin!r} marker in {path.relative_to(ROOT)}, found {begin_count}")
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
    _validate_core_payload(core_text, plain_text)

    # Validate and stage every updated target in memory before writing anything to disk.
    staged: list[tuple[Path, str]] = []
    for path in MD_ADAPTERS:
        current = read_utf8_no_bom(path)
        updated = replace_block(current, MD_BEGIN, MD_END, core_text, path)
        staged.append((path, updated))

    txt_current = read_utf8_no_bom(TXT_ADAPTER)
    staged.append((TXT_ADAPTER, replace_block(txt_current, TXT_BEGIN, TXT_END, plain_text, TXT_ADAPTER)))

    html_current = read_utf8_no_bom(HTML_ADAPTER)
    staged.append((HTML_ADAPTER, replace_block(html_current, HTML_BEGIN, HTML_END, plain_text, HTML_ADAPTER)))

    for path, updated in staged:
        write_utf8_lf(path, updated)
        print(f"SYNCED: {path.relative_to(ROOT)}")
    return 0


def do_check() -> int:
    failures: list[str] = []
    passes: list[str] = []

    def fail(msg: str) -> None:
        failures.append(msg)

    def ok(msg: str) -> None:
        passes.append(msg)

    # 1. Core budget check
    core_text = ""
    plain_text = ""
    if not CORE_PATH.is_file():
        fail("Check 1: core/micro-rule.md does not exist")
    else:
        try:
            core_text = read_utf8_no_bom(CORE_PATH).strip()
            plain_text = strip_markdown_to_plain(core_text)
            _validate_core_payload(core_text, plain_text)
            non_empty_lines = [ln for ln in core_text.splitlines() if ln.strip()]
            byte_len = len(core_text.encode("utf-8"))
            ok(
                f"Check 1 PASS: core/micro-rule.md = {len(non_empty_lines)} non-empty lines, "
                f"{byte_len} UTF-8 bytes (<= 35 lines, <= 2000 bytes)"
            )
        except (ValueError, UnicodeDecodeError) as exc:
            fail(f"Check 1: {exc}")

    # 2. Adapter sync parity check
    drift_items: list[str] = []
    for path in MD_ADAPTERS:
        if not path.is_file():
            drift_items.append(f"missing {path.relative_to(ROOT)}")
            continue
        try:
            content = read_utf8_no_bom(path)
            expected = replace_block(content, MD_BEGIN, MD_END, core_text, path).rstrip("\n") + "\n"
            if content != expected:
                drift_items.append(f"drift in {path.relative_to(ROOT)}")
        except (ValueError, UnicodeDecodeError) as exc:
            drift_items.append(str(exc))
    if not TXT_ADAPTER.is_file():
        drift_items.append(f"missing {TXT_ADAPTER.relative_to(ROOT)}")
    else:
        try:
            txt_content = read_utf8_no_bom(TXT_ADAPTER)
            txt_expected = replace_block(txt_content, TXT_BEGIN, TXT_END, plain_text, TXT_ADAPTER).rstrip("\n") + "\n"
            if txt_content != txt_expected:
                drift_items.append(f"drift in {TXT_ADAPTER.relative_to(ROOT)}")
        except (ValueError, UnicodeDecodeError) as exc:
            drift_items.append(str(exc))
    if not HTML_ADAPTER.is_file():
        drift_items.append(f"missing {HTML_ADAPTER.relative_to(ROOT)}")
    else:
        try:
            html_content = read_utf8_no_bom(HTML_ADAPTER)
            html_expected = replace_block(html_content, HTML_BEGIN, HTML_END, plain_text, HTML_ADAPTER).rstrip("\n") + "\n"
            if html_content != html_expected:
                drift_items.append(f"drift in {HTML_ADAPTER.relative_to(ROOT)}")
        except (ValueError, UnicodeDecodeError) as exc:
            drift_items.append(str(exc))
    if drift_items:
        fail("Check 2: adapter sync mismatch -> " + "; ".join(drift_items))
    else:
        ok(f"Check 2 PASS: all {len(MD_ADAPTERS) + 2} adapters match core/micro-rule.md with zero drift")

    # 3. rules/AGENTS.md must NOT have YAML frontmatter
    agents_rule_path = ROOT / "rules" / "AGENTS.md"
    if not agents_rule_path.is_file():
        fail("Check 3: rules/AGENTS.md missing")
    else:
        try:
            agents_rule = read_utf8_no_bom(agents_rule_path)
            if agents_rule.lstrip().startswith("---"):
                fail("Check 3: rules/AGENTS.md must NOT start with YAML frontmatter '---'")
            else:
                ok("Check 3 PASS: rules/AGENTS.md is plain Markdown without YAML frontmatter")
        except (ValueError, UnicodeDecodeError) as exc:
            fail(f"Check 3: {exc}")

    # 4. Web custom instructions char count <= 1500 & exact length parity with start.html
    if TXT_ADAPTER.is_file():
        try:
            stripped_body = extract_block(read_utf8_no_bom(TXT_ADAPTER), TXT_BEGIN, TXT_END, TXT_ADAPTER)
            char_len = len(stripped_body)
            if char_len > 1500 or (plain_text and stripped_body != plain_text):
                fail(f"Check 4: adapters/web-custom-instructions.txt mismatch or char_len={char_len} > 1500")
            else:
                ok(f"Check 4 PASS: web-custom-instructions.txt stripped body = {char_len} chars (<= 1500, exact core parity)")
        except (ValueError, UnicodeDecodeError) as exc:
            fail(f"Check 4: {exc}")

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

    # 8. Offline self-contained HTML, inline SVG, and start.html UI contract check
    yaml_template_path = ROOT / "templates" / "cells-alive.yaml.example"
    scalar_yaml_keys: list[str] = []
    if yaml_template_path.is_file():
        for ln in read_utf8_no_bom(yaml_template_path).splitlines():
            m_k = re.match(r"^([a-z_]+):\s*\S+", ln)
            if m_k:
                scalar_yaml_keys.append(m_k.group(1))
    for html_path in (ROOT / "examples" / "04-internal-summary-note.html", HTML_ADAPTER):
        rel_html = html_path.relative_to(ROOT)
        if not html_path.is_file():
            fail(f"Check 8: {rel_html} missing")
            continue
        try:
            html_text = read_utf8_no_bom(html_path)
        except (ValueError, UnicodeDecodeError) as exc:
            fail(f"Check 8: {rel_html} encoding error: {exc}")
            continue
        html_issues: list[str] = []
        ext_hits = EXTERNAL_ASSET_RE.findall(html_text)
        if ext_hits:
            html_issues.append(f"external/network dependencies {ext_hits}")
        for svg_m in re.finditer(r"<svg\b[^>]*>.*?</svg>", html_text, re.IGNORECASE | re.DOTALL):
            cleaned_svg = SVG_ALLOWED_XMLNS_RE.sub("", svg_m.group(0))
            bad_svg = SVG_FORBIDDEN_RE.search(cleaned_svg)
            if bad_svg:
                html_issues.append(f"unsafe inline <svg> construct {bad_svg.group(0)!r}")
        if html_path == HTML_ADAPTER:
            if re.search(r"<input\b[^>]*\btype\s*=\s*['\"]?radio\b", html_text, re.IGNORECASE):
                html_issues.append("forbidden radio input detected")
            for req_id in ("cfg-tone", "cfg-role", "cfg-track", "cfg-humor", "yaml-preview"):
                if f'id="{req_id}"' not in html_text:
                    html_issues.append(f"missing #{req_id} YAML builder element")
            missing_keys = [k for k in scalar_yaml_keys if f"{k}:" not in html_text]
            if missing_keys:
                html_issues.append(f"start.html YAML builder missing template keys {missing_keys}")
            try:
                embedded_rules = extract_block(html_text, HTML_BEGIN, HTML_END, HTML_ADAPTER)
                if plain_text and embedded_rules != plain_text:
                    html_issues.append("embedded #rules does not match core plain text")
            except ValueError as exc:
                html_issues.append(str(exc))
        if html_issues:
            fail(f"Check 8: {rel_html} -> " + "; ".join(html_issues))
        else:
            extra = (
                f", 0 radios, <select> YAML builder ({len(scalar_yaml_keys)} keys), {len(plain_text)}-char local rules"
                if html_path == HTML_ADAPTER
                else ""
            )
            ok(f"Check 8 PASS: {rel_html} offline/inline-SVG hygiene passed{extra}")

    # 9. Repository-wide placeholder & BOM scan
    scan_targets = [
        ROOT / "package.json",
        ROOT / "README.md",
        ROOT / "README.en.md",
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
        try:
            svg_text = read_utf8_no_bom(svg_path)
        except (ValueError, UnicodeDecodeError) as exc:
            svg_issues.append(f"{svg_path.relative_to(ROOT)} encoding error: {exc}")
            continue
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
        try:
            text = read_utf8_no_bom(fpath)
        except (ValueError, UnicodeDecodeError) as exc:
            legacy_hits.append(f"{fpath.relative_to(ROOT)} ({exc})")
            continue
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
