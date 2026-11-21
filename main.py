#!/usr/bin/env python3
"""Roof mat - an entry for make.fun's "Make the AI judge feel awe" bounty.

Running this script writes the entry text to /output/entry.txt.
The text is a short rooftop scene: a child lying beside their father,
watching a falling star whose light is older than the village itself.
Revised after a Gemini critique round on the original draft.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "You lie on the roof mat beside your father.\n"
    "His arm is your pillow.\n"
    "The tiles still hold the day's heat.\n"
    "A star falls. No wish. He watches.\n"
    "The sky keeps opening.\n"
    "Its light set out before this village had a name,\n"
    "before the roof, before the mat,\n"
    "and it is still arriving.\n"
)


def main() -> None:
    # The bounty accepts entry texts of 1-280 Unicode code points.
    points = len(TEXT)
    assert 1 <= points <= 280, f"entry text is {points} code points"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
