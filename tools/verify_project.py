#!/usr/bin/env python3
"""Verify the public package without installing or contacting anything."""
import ast
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "comedy-workbench"
spec = importlib.util.spec_from_file_location("cw_verify", SKILL / "scripts" / "comedy_workbench.py")
cw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cw)


def verify():
    checks, errors = [], []
    excluded = {".git", "__pycache__", "dist", ".venv"}
    files = [p for p in ROOT.rglob("*") if p.is_file() and not any(part in excluded for part in p.relative_to(ROOT).parts)]
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix in {".py", ".md", ".json", ".yaml", ".yml"} or path.name in {"LICENSE", ".gitignore", ".gitattributes"}:
            text = path.read_text(encoding="utf-8")
            if re.search(r"[A-Z]:[\\/]Users[\\/]", text):
                errors.append(f"Private machine path in {relative}")
        else:
            errors.append(f"Unexpected public artifact: {relative}")
            continue
        if path.suffix == ".py":
            ast.parse(text, filename=relative)
            checks.append("syntax:" + relative)
        if path.suffix == ".md":
            for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", text):
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                destination = unquote(target.strip("<>").split("#", 1)[0])
                if not (path.parent / destination).resolve().exists():
                    errors.append(f"Broken link in {relative}: {target}")
            if "[TODO:" in text:
                errors.append(f"Unfinished scaffold in {relative}")
            checks.append("links:" + relative)
        if path.suffix == ".json":
            data = cw.parse_json(text)
            if isinstance(data, dict) and "schema_version" in data:
                cw.validate_project(data)
                cw.analyze(data)
                checks.append("project:" + relative)
    entrypoint = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not entrypoint.startswith("---\nname: comedy-workbench\ndescription:"):
        errors.append("Skill metadata does not match package identity")
    if (ROOT / "LICENSE").read_bytes() != (SKILL / "LICENSE").read_bytes():
        errors.append("Standalone skill license missing or different")
    catalogue = json.loads((ROOT / "research" / "sources.json").read_text(encoding="utf-8"))
    for source in catalogue["sources"]:
        if source.get("status") == "downloaded" and not re.fullmatch(r"[0-9a-f]{64}", source.get("sha256", "")):
            errors.append("Missing download digest: " + source["id"])
        if source.get("kind") == "repository" and source.get("status") == "downloaded":
            if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
                errors.append("Missing commit pin: " + source["id"])
            if not source.get("inspected_files"):
                errors.append("Missing scoped source study: " + source["id"])
    checks.append("provenance-metadata")
    observation = cw.parse_json((ROOT / "examples" / "rehearsal-synthetic.json").read_text(encoding="utf-8"))
    short = cw.parse_json((ROOT / "examples" / "short.json").read_text(encoding="utf-8"))
    if any(e["reported_laughter_seconds"] is not None for e in cw.rehearsal(short, observation)["events"]):
        errors.append("Synthetic fixture was represented as live audience evidence")
    checks.append("rehearsal-provenance")
    print(json.dumps({"files_checked": len(files), "checks": len(checks), "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(verify())
