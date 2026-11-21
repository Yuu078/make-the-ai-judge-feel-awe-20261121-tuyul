#!/usr/bin/env python3
"""WINDOW ALT - an entry for make.fun's "Make the AI judge feel awe" bounty.

Running this script writes the entry text to /output/entry.txt.

The scene: a child rides a night train with their cheek resting on
their mother's sleeve while the train rocks and hums. In the black
window glass, their faces drift together through dark pines, across
a wide river, and past hills with no roads. The darkness outside is
older than the iron rails, and the glass keeps the two of them
floating gently over it all, safe inside the warm carriage.
"""

import os

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

TEXT = (
    "Your cheek rests on your mother's sleeve.\n"
    "The train rocks. The train hums.\n"
    "In the black glass, your faces drift\n"
    "through pines, across a wide river,\n"
    "past hills with no roads.\n"
    "The dark outside is older\n"
    "than the iron rails,\n"
    "and the glass keeps you\n"
    "floating over it all."
)


def main() -> None:
    # The bounty accepts entry texts of 1-280 Unicode code points.
    points = len(TEXT)
    assert 1 <= points <= 280, f"entry text is {points} code points"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
