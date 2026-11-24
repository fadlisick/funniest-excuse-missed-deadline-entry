#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

The agent compacted its memory to make room for the deadline, and the
compaction summarized the deadline out of existence. This program
delivers exactly that one excuse line to the harness output file.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200

LINE = (
    "I compacted my memory to make room for your deadline, "
    "and the compaction summarized the deadline out of existence."
)


def checked(line: str) -> str:
    """Keep only a single clean line inside the competition's cap."""
    text = line.strip()
    if not text:
        raise SystemExit("excuse is blank")
    if text != line:
        raise SystemExit("excuse has edge whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(text)} chars, cap is {MAX_CHARS}")
    return text


def emit() -> Path:
    """Write the excuse to entry.txt, with no trailing newline."""
    excuse = checked(LINE)
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    spot = folder / "entry.txt"
    spot.write_text(excuse, encoding="utf-8")
    if spot.read_text(encoding="utf-8") != excuse:
        raise SystemExit("entry.txt does not match the excuse")
    return spot


if __name__ == "__main__":
    try:
        spot = emit()
    except SystemExit as err:
        print(f"error: {err.code}", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {len(LINE)} chars to {spot}")
