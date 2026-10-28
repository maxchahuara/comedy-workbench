#!/usr/bin/env python3
"""Run the bundled tool without installing a package or a skill."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "skills" / "comedy-workbench" /
                       "scripts" / "comedy_workbench.py"), run_name="__main__")
