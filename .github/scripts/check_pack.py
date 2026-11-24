#!/usr/bin/env python3
"""Checks a pull request against the rules for the LAPGCCraft pack."""
import glob
import json
import os
import re
import subprocess
import sys

BASE = os.environ["BASE_SHA"]
HEAD = os.environ["HEAD_SHA"]
MAX_BYTES = 50 * 1024 * 1024
ALLOWED_JAR = "overrides/packweaver.jar"

PERSONAL_PATTERNS = [
    r"^overrides/journeymap/",
    r"^overrides/options\.txt$",
    r"^overrides/servers\.dat$",
    r"^overrides/saves/",
    r"^overrides/logs/",
    r"^overrides/crash-reports/",
    r"^overrides/screenshots/",
    r"^overrides/kubejsstudio/",
    r"^overrides/config/kubejsstudio/",
    r"^overrides/rhino\.local\.properties$",
    r"^overrides/.*\.zip$",
    r"^overrides/.*\.bak$",
    r"^overrides/config/.*\.bak$",
    r"(^|/)server\.properties$",
    r"(^|/)eula\.txt$",
    r"(^|/)ops\.json$",
    r"(^|/)whitelist\.json$",
    r"(^|/)banned-(ips|players)\.json$",
    r"(^|/)usercache\.json$",
    r"(^|/)usernamecache\.json$",
    r"\.log$",
]

errors = []


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


changed = []
for line in git("diff", "--name-status", "--no-renames", BASE, HEAD).splitlines():
    status, _, path = line.partition("\t")
    changed.append((status, path))

for status, path in changed:
    if status == "D":
        continue
    for pattern in PERSONAL_PATTERNS:
        if re.search(pattern, path):
            errors.append(f"{path}: personal or server-only file. Remove it from your change.")
            break
    if path.endswith(".jar") and path != ALLOWED_JAR:
        errors.append(
            f"{path}: mod jars can't be committed by hand. Add the mod through Packweave so its "
            "metadata is recorded in content/mods/."
        )
    if os.path.exists(path):
        size = os.path.getsize(path)
        if size > MAX_BYTES:
            errors.append(f"{path}: {size // (1024 * 1024)} MB. Files over 50 MB aren't allowed.")
    if path.endswith(".json") and os.path.exists(path):
        try:
            json.load(open(path, encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{path}: not valid JSON ({exc}).")

names = {}
for path in sorted(glob.glob("content/mods/*.json")):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except ValueError as exc:
        errors.append(f"{path}: not valid JSON ({exc}).")
        continue
    if data.get("disabled") or data.get("serverSide") == "unsupported":
        continue
    sources = data.get("sources", {})
    if not sources:
        errors.append(f"{path}: no download source.")
        continue
    for source_name, source in sources.items():
        if not source.get("sha1") or not source.get("downloadUrl") or not source.get("filename"):
            errors.append(f"{path}: {source_name} source is missing filename, downloadUrl, or sha1.")
    preferred = data.get("preferred")
    source = sources.get(preferred) or next(iter(sources.values()))
    filename = source.get("filename", "")
    if filename in names:
        errors.append(
            f"{path} and {names[filename]} both download {filename}. "
            "Remove one of them, or link them as alternate sources in Packweave."
        )
    names[filename] = path

if errors:
    print("This pull request can't be merged yet:\n")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"All checks passed for {len(changed)} changed file(s).")
