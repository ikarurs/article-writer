#!/usr/bin/env python3
"""Check that an article package has the required reproducible shape."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_FILES = [
    "article.yaml",
    "README.md",
    "sources/source-log.md",
    "sources/citations.bib",
    "analysis/analysis.py",
    "outputs/findings.md",
    "writing/outline.md",
    "writing/notes.md",
]

REQUIRED_DIRS = [
    "sources",
    "data/raw",
    "data/processed",
    "analysis",
    "outputs/figures",
    "outputs/tables",
    "writing",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package")
    args = parser.parse_args()

    package = Path(args.package)
    missing = []
    for directory in REQUIRED_DIRS:
        if not (package / directory).is_dir():
            missing.append(f"dir: {directory}")
    for file in REQUIRED_FILES:
        if not (package / file).is_file():
            missing.append(f"file: {file}")

    if missing:
        print("missing required package entries:")
        for item in missing:
            print(f"- {item}")
        return 1

    print(f"ok: {package.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
