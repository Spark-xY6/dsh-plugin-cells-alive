#!/usr/bin/env python3
"""Release gate verification for dsh-plugin-cells-alive."""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.resolve()
SYNC_SCRIPT = REPO_ROOT / "scripts" / "sync_adapters.py"
BINARY_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico"}

LOCAL_PATH_PATTERNS = [
    re.compile(r"[A-Za-z]:[/\\]Users[/\\]", re.IGNORECASE),
    re.compile(r"D:[/\\]" + bytes.fromhex("616e61636f6e646133").decode("utf-8"), re.IGNORECASE),
]

# Hex-encoded blocklist terms so no restricted identifier appears literally in tests.
BLOCKED_TERMS_CI = [
    bytes.fromhex("6c656e6f766f").decode("utf-8"),
    bytes.fromhex("616e61636f6e646133").decode("utf-8"),
    bytes.fromhex("e58c97e4baace5a4a7e5ada6").decode("utf-8"),
    bytes.fromhex("70656b696e6720756e6976657273697479").decode("utf-8"),
    bytes.fromhex("e5a79ae58d93e68890").decode("utf-8"),
    bytes.fromhex("e5ad99e58583e5bcba").decode("utf-8"),
    bytes.fromhex("e99988e5bf83e682a6").decode("utf-8"),
]

REQUIRED_YAML_KEYS = [
    "tone_style",
    "role_stage",
    "dosage",
    "time_awareness",
    "light_humor",
    "internal_md_html_note",
    "research_track",
]

EXPECTED_EXAMPLES = [
    "01-setback-care-and-pivot.md",
    "02-calm-data-no-presumption.md",
    "03-boundary-pushback-outlier.md",
    "04-internal-summary-note.md",
    "04-internal-summary-note.html",
    "05-manuscript-zero-leak.md",
    "06-wonder-curiosity-and-late-night.md",
    "07-outcome-driven-and-chill-pause.md",
]


def gate_1_sync_checks() -> None:
    proc = subprocess.run(
        [sys.executable, "-B", "-X", "utf8", str(SYNC_SCRIPT), "--check"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        raise AssertionError(
            f"GATE-1 failed (rc={proc.returncode}):\n{proc.stdout}\n{proc.stderr}"
        )
    print("GATE-1 PASS: scripts/sync_adapters.py --check exited 0 (all 11 checks)")


def gate_2_deid_and_hygiene() -> None:
    stray_artifacts: list[str] = []
    leaks: list[str] = []

    for directory, dirs, names in os.walk(REPO_ROOT):
        dirs[:] = sorted(d for d in dirs if d not in {".git", "node_modules"})
        for name in sorted(names):
            p = pathlib.Path(directory, name)
            rel = p.relative_to(REPO_ROOT).as_posix()
            if "__pycache__" in p.parts or p.suffix.lower() in (".pyc", ".tgz"):
                stray_artifacts.append(rel)
                continue
            for pat in LOCAL_PATH_PATTERNS:
                m = pat.search(rel)
                if m:
                    leaks.append(f"{rel} path matched local path {m.group(0)!r}")
            if p.suffix.lower() in BINARY_EXTS:
                continue
            txt = p.read_text(encoding="utf-8")
            for pat in LOCAL_PATH_PATTERNS:
                m = pat.search(txt)
                if m:
                    leaks.append(f"{rel} matched local path {m.group(0)!r}")
            low = txt.lower()
            for term in BLOCKED_TERMS_CI:
                if term in low:
                    leaks.append(f"{rel} matched restricted term ({len(term)} chars)")

    assert not stray_artifacts, f"Stray build/temp artifacts in repo: {stray_artifacts}"
    assert not leaks, f"De-identification / path leak check failed: {leaks}"

    pkg = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    missing_pkg_entries: list[str] = []
    for entry in pkg.get("files", []):
        if "*" in entry:
            matches = list(REPO_ROOT.glob(entry))
            if not matches:
                missing_pkg_entries.append(entry)
        else:
            if not (REPO_ROOT / entry).exists():
                missing_pkg_entries.append(entry)
    assert not missing_pkg_entries, f"Missing package.json files entries: {missing_pkg_entries}"
    print(f"GATE-2 PASS: repo hygiene & de-identification clean ({len(pkg.get('files', []))} package.json file entries verified)")


def gate_3_config_and_showcase() -> None:
    cfg_text = (REPO_ROOT / "templates" / "cells-alive.yaml.example").read_text(encoding="utf-8")
    missing_keys = [k for k in REQUIRED_YAML_KEYS if f"{k}:" not in cfg_text]
    assert not missing_keys, f"Missing keys in cells-alive.yaml.example: {missing_keys}"

    showcase_path = REPO_ROOT / "docs" / "comparison-and-showcase.md"
    assert showcase_path.is_file(), "Missing docs/comparison-and-showcase.md"

    examples_dir = REPO_ROOT / "examples"
    missing_examples = [name for name in EXPECTED_EXAMPLES if not (examples_dir / name).is_file()]
    assert not missing_examples, f"Missing example files: {missing_examples}"

    print(
        f"GATE-3 PASS: {len(REQUIRED_YAML_KEYS)} config keys, comparison-and-showcase.md, "
        f"and {len(EXPECTED_EXAMPLES)} example files verified"
    )


def main() -> int:
    gate_1_sync_checks()
    gate_2_deid_and_hygiene()
    gate_3_config_and_showcase()
    print("ALL 3 RELEASE GATES PASSED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
