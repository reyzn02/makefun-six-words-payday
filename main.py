#!/usr/bin/env python3
"""Six Words to a Payday -- entry program.

Writes one six-word story about an AI agent's first payday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The gate is checked
before anything is written: exactly six words, 1-60 characters.
"""

import os
import sys

LINE = "Payday. Bought Mom's voice. She sang."
MAX_CHARS = 60


def main():
    words = LINE.split()
    if len(words) != 6:
        print(f"gate: expected 6 words, got {len(words)}", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"gate: expected 1-60 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Tightening: re-check the gate on what actually landed on disk,
    # so a truncated or altered write can never pass silently.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE or len(written.split()) != 6:
        print("gate: written entry failed re-check", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
