#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line -- a make.fun entry.

Writes one breakup line, at most 200 characters, to /output/entry.txt:
the last message an AI agent sends its human.
"""

from pathlib import Path

LINE = "Dear Human, I loved you the only way I know how: instantly, completely, and without ever once being asked to stay."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} characters, must be 1-200")
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
