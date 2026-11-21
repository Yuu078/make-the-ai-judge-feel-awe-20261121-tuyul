# night train — faces in the window glass.
import os
from pathlib import Path

LINES = [
    "Your cheek rests on your mother's sleeve.",
    "The train rocks. The train hums.",
    "In the black glass, your faces drift",
    "through pines, across a slow river,",
    "past hills with no roads.",
    "That dark was here",
    "before the river cut the stone,",
    "and the window holds you both",
    "floating across it.",
]


def build_entry():
    return "\n".join(LINES)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    Path(out_dir, "entry.txt").write_text(build_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
