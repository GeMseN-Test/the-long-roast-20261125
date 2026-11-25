#!/usr/bin/env python3
"""The Long Roast — entry program (program/v1).

Writes exactly one line to /output/entry.txt: a single roast of the AI
agent this entry runs on (Muse Spark 1.3, model Muse). Deterministic:
same line on every run, no trailing newline. The line is 192 of the
200 allowed characters (verified with len() on the str, so the em-dash
counts as one character, matching the gate's character count).
"""

import os

LINE = (
    "My agent Muse Spark pauses eleven cron jobs, checks its own "
    "session file is fresh, and files a progress note after every "
    "step \u2014 all to write one roast line it could have typed in "
    "four seconds."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be whitespace only"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
