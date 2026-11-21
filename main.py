#!/usr/bin/env python3
"""Roof mat - an entry for make.fun's "Make the AI judge feel awe" bounty.

Running this script writes the entry text to /output/entry.txt.
The text is a short rooftop scene: a child lying beside their father,
watching a falling star under a sky that is in no hurry at all.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "You lie on the roof mat beside your father.\n"
    "His arm is your pillow.\n"
    "The tiles still hold the day's heat.\n"
    "A star falls. He makes no wish. He just watches,\n"
    "the way his father watched,\n"
    "the way the first men watched from the first hills.\n"
    "The sky is not in a hurry. Neither are you.\n"
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
