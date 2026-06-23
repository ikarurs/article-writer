#!/usr/bin/env python3
"""Create one reproducible article research package."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


def slugify(topic: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
    return slug or "untitled"


def write(path: Path, text: str) -> None:
    if path.exists():
        return
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--root", default="articles")
    args = parser.parse_args()

    package = Path(args.root) / f"{args.date}-{slugify(args.topic)}"
    dirs = [
        "sources",
        "data/raw",
        "data/processed",
        "analysis",
        "outputs/figures",
        "outputs/tables",
        "writing",
    ]
    for directory in dirs:
        (package / directory).mkdir(parents=True, exist_ok=True)

    write(
        package / "article.yaml",
        f"""topic: "{args.topic.replace('"', '\\"')}"
date: "{args.date}"
package: "{package.as_posix()}"
sources: []
commands_run: []
agent_notes:
  subagent_mode: "unknown"
reproducibility:
  status: "draft"
  notes: ""
""",
    )
    write(package / "README.md", f"# {args.topic}\n\nReproducible research package.\n")
    write(package / "sources" / "source-log.md", "# Source Log\n\n")
    write(package / "sources" / "citations.bib", "")
    write(
        package / "analysis" / "analysis.py",
        """#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    print(f"analysis package: {ROOT}")


if __name__ == "__main__":
    main()
""",
    )
    write(package / "analysis" / "proposals.md", "# Analysis Proposals\n\n")
    write(package / "analysis" / "judgments.md", "# Analysis Judgments\n\n")
    write(package / "analysis" / "selected-analysis.md", "# Selected Analysis Plan\n\n")
    write(package / "outputs" / "findings.md", "# Findings\n\n")
    write(package / "writing" / "outline.md", "# Outline\n\n")
    write(package / "writing" / "notes.md", "# Notes\n\n")
    print(package.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
