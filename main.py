#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes one line — a single-line joke about office life — to
/output/entry.txt.
"""

import os
import sys

LINE = (
    "Our 15-minute quick sync needed a pre-meeting, a follow-up, "
    "and a meeting to discuss the meeting."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def valid_line(text: str) -> bool:
    """True only for a single non-empty line within the limit."""
    if not text:
        return False
    if len(text) > 200:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> int:
    # Validate the line before writing: one line, 1-200 chars, not blank.
    text = LINE.strip()
    if not valid_line(text):
        print(
            f"invalid entry line: {len(text)} chars",
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Open the file back up and confirm it holds exactly the entry line
    # followed by one newline, with nothing extra slipped in.
    expected = text + "\n"
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != expected:
        print("written entry failed validation", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
