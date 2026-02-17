import json
import os
from typing import Dict

FILENAME = "students.json"


def load_students(filename: str) -> Dict[str, float]:
    """Load students dict from JSON file. Return {} if file missing/corrupted."""
    if not os.path.exists(filename):
        print("No existing file. Starting new.")
        return {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Ensure values are floats (json may load int/float)
        students: Dict[str, float] = {}
        for name, score in data.items():
            students[str(name)] = float(score)

        print("Loaded existing data.")
        return students

    except json.JSONDecodeError:
        print("⚠ JSON file corrupted. Starting fresh.")
        return {}
    except OSError as e:
        print(f"⚠ Failed to read file: {e}. Starting fresh.")
        return {}
    except (TypeError, ValueError) as e:
        print(f"⚠ Invalid data format: {e}. Starting fresh.")
        return {}


def save_students(filename: str, students: Dict[str, float]) -> None:
    """Save students dict to JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(students, file, ensure_ascii=False, indent=4)
        print("Saved successfully.")
    except OSError as e:
        print(f"❌ Save failed: {e}")


def input_int(prompt: str) -> int:
    """Read an integer safely."""
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("⚠ Please enter a valid integer (e.g. 3).")


def input_float(prompt: str) -> float:
    """Read a float safely."""
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠ Please enter a valid number (e.g. 88 or 78.5).")


def input_nonempty(prompt: str) -> str:
    """Read a non-empty string."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("⚠ Name cannot be empty.")


def add_students(students: Dict[str, float]) -> None:
    """Ask user to add/update multiple students."""
    count = input_int("How many students to add/update? ")
    if count <= 0:
        print("Nothing to add.")
        return

    for _ in range(count):
        name = input_nonempty("Enter name: ")
        score = input_float("Enter score: ")
        existed = name in students
        students[name] = score
        print("✅ Updated." if existed else "✅ Added.")


def print_students(students: Dict[str, float]) -> None:
    """Print students dict in a readable way."""
    if not students:
        print("📭 No students data.")
        return

    print("\nStudent Scores:")
    for name, score in students.items():
        print(f"- {name}: {score}")


def main() -> None:
    students = load_students(FILENAME)

    add_students(students)

    save_students(FILENAME, students)

    # Read back for verification (optional)
    loaded_again = load_students(FILENAME)
    print_students(loaded_again)


if __name__ == "__main__":
    main()