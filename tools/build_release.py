#!/usr/bin/env python3
"""Build deterministic ZIPs, then exercise the extracted standalone skill."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "comedy-workbench"
VERSION = "0.1.0"
EXCLUDED = {".git", "__pycache__", "dist", ".venv"}


def archive(source, destination, prefix):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(source.rglob("*")):
            if not path.is_file() or any(part in EXCLUDED for part in path.relative_to(source).parts):
                continue
            entry = zipfile.ZipInfo(prefix + "/" + path.relative_to(source).as_posix(), (2026, 10, 28, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, path.read_bytes())


def main():
    subprocess.run([sys.executable, str(ROOT / "tools" / "verify_project.py")], check=True, cwd=ROOT)
    destination = ROOT / "dist"
    destination.mkdir(exist_ok=True)
    skill_zip = destination / f"comedy-workbench-skill-{VERSION}.zip"
    repository_zip = destination / f"comedy-workbench-{VERSION}.zip"
    archive(SKILL, skill_zip, "comedy-workbench")
    archive(ROOT, repository_zip, "comedy-workbench")
    with tempfile.TemporaryDirectory() as temporary:
        folder = Path(temporary)
        with zipfile.ZipFile(skill_zip) as bundle:
            bundle.extractall(folder)
        script = folder / "comedy-workbench" / "scripts" / "comedy_workbench.py"
        new_draft = folder / "draft.json"
        subprocess.run([sys.executable, str(script), "new", "short", str(new_draft)], check=True, cwd=folder)
        subprocess.run([sys.executable, str(script), "check", str(new_draft), "--output-format", "json"],
                       check=True, cwd=folder, stdout=subprocess.DEVNULL)
        subprocess.run([sys.executable, str(script), "review-pack", str(new_draft), str(folder / "review")],
                       check=True, cwd=folder, stdout=subprocess.DEVNULL)
    records = [{"file": path.name, "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in (repository_zip, skill_zip)]
    (destination / "checksums.json").write_text(json.dumps({"version": VERSION, "standalone_smoke_test": "passed", "artifacts": records}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
