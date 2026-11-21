# entry: night train, faces in glass
import os

VERSES = (
    "Your cheek rests on your mother's sleeve.",
    "The train rocks. The train hums.",
    "In the black glass, your faces drift",
    "through pines, across a slow river,",
    "past hills with no roads.",
    "That dark was here",
    "before the river cut the stone,",
    "and the window holds you both",
    "floating across it.",
)


def compose_entry():
    return "\n".join(VERSES)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = compose_entry()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
