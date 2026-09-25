from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INCLUDE_DIRS = [
    "principles",
    "design",
    "coding",
    "naming",
    "anti-patterns",
    "checklist",
]

OUTPUT_DIR = ROOT / "export"
OUTPUT_FILE = OUTPUT_DIR / "eltech-method.txt"


def append_file(out, filepath: Path):
    rel = filepath.relative_to(ROOT)

    out.write("\n")
    out.write("=" * 80 + "\n")
    out.write(f"FILE: {rel}\n")
    out.write("=" * 80 + "\n\n")

    out.write(
        filepath.read_text(
            encoding="utf-8",
            errors="replace"
        )
    )

    out.write("\n")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:

        # README
        readme = ROOT / "README.md"

        if readme.exists():
            append_file(out, readme)

        # 各ディレクトリ
        for dirname in INCLUDE_DIRS:

            folder = ROOT / dirname

            if not folder.exists():
                continue

            for md_file in sorted(folder.rglob("*.md")):
                append_file(out, md_file)

    print(f"generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()