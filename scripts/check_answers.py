"""Simple checker for the Git Recovery Practice repo.

This is intentionally tiny and beginner-friendly.
It checks that the final conflict line in files/story.md matches the expected value.
"""

from pathlib import Path

EXPECTED = "LINE_TO_CONFLICT: Student A and Student B were here."

def main() -> None:
    story_path = Path(__file__).resolve().parents[1] / "files" / "story.md"
    text = story_path.read_text(encoding="utf-8").splitlines()

    found = [line.strip() for line in text if line.strip().startswith("LINE_TO_CONFLICT:")]
    if not found:
        print("FAIL: Could not find a LINE_TO_CONFLICT line.")
        return

    # Use the last occurrence, in case students accidentally duplicated it
    actual = found[-1]
    if actual == EXPECTED:
        print("PASS: Conflict line matches expected final resolution.")
    else:
        print("FAIL: Conflict line does not match expected.")
        print(f"Expected: {EXPECTED}")
        print(f"Actual:   {actual}")

if __name__ == "__main__":
    main()
