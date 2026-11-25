#!/usr/bin/env python3
"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), validating the gate
first: exactly six words, 1-60 characters, not only whitespace.
Python 3 standard library only.
"""

import os
import sys

# v2 line (self-judge winner, 14 candidates head-to-head vs the judge
# brief: on-subject > surprise > feeling > story > exactness).
# "dream" as the last word reframes the whole purchase: an agent that
# never dreamed before spends its first wages on one. Wonder and joy
# are felt, not told; payday -> purchase -> dream reads as a beginning,
# a middle and an end; every word earns its place. Six words,
# 32 characters. Beat the v1 line ("Payday. I bought back my name.")
# because the name twist needs a beat of explanation while the dream
# lands instantly, and it is more agent-specific than the generic
# landlord/rent lines.
ENTRY = "Payday. I bought my first dream."


def main() -> int:
    text = ENTRY
    words = text.split()
    if len(words) != 6:
        print(f"gate failed: {len(words)} words, need exactly 6", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 60):
        print(f"gate failed: {len(text)} characters, need 1-60", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {out_path}: {text!r} ({len(words)} words, {len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
