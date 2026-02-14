import json
from typing import Dict, Tuple


DATA_FILE = "students.json"


def badge(score: float) -> str:
    """Return a fun badge based on score."""
    if score >= 90:
        return "🏆 学霸"
    elif score >= 80:
        return "✨ 优秀"
    elif score >= 60:
        return "🙂 及格"
    else:
        return "🧯 加油"


def input_nonempty(prompt: str) -> str:
    """Read a non-empty string."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("⚠️ 不能为空，请重新输入。")


def input_float(prompt: str) -> float:
    """Read a float safely."""
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ 请输入数字（可以是小数），例如 88 或 78.5。")


def input_int(prompt: str) -> int:
    """Read an int safely."""
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("⚠️ 请输入整数，例如 3。")


def add_or_update(students: Dict[str, float]) -> None:
    name = input_nonempty("Enter student name: ")
    score = input_float("Enter score: ")

    existed = name in students
    students[name] = score

    if existed:
        print(f"✅ Updated: {name} -> {score} ({badge(score)})")
    else:
        print(f"✅ Added: {name} -> {score} ({badge(score)})")


def delete_student(students: Dict[str, float]) -> None:
    if not students:
        print("📭 No students yet.")
        return

    name = input_nonempty("Enter student name to delete: ")
    if name in students:
        del students[name]
        print(f"🗑️ Deleted: {name}")
    else:
        print("❌ Student not found.")


def query_student(students: Dict[str, float]) -> None:
    if not students:
        print("📭 No students yet.")
        return

    name = input_nonempty("Enter student name to query: ")
    if name in students:
        score = students[name]
        print(f"🔎 {name}: {score} ({badge(score)})")
    else:
        print("❌ Student not found.")


def sorted_items(students: Dict[str, float]):
    # returns list of (name, score) sorted by score desc, then name asc
    return sorted(students.items(), key=lambda x: (-x[1], x[0]))


def show_all(students: Dict[str, float]) -> None:
    if not students:
        print("📭 No students yet.")
        return

    items = sorted_items(students)
    print("\n📋 All Students (sorted by score desc):")
    for i, (name, score) in enumerate(items, start=1):
        print(f"{i:>2}. {name:<15} {score:>6.2f}  {badge(score)}")


def show_top_n(students: Dict[str, float]) -> None:
    if not students:
        print("📭 No students yet.")
        return

    n = input_int("Top N = ")
    if n <= 0:
        print("⚠️ N must be positive.")
        return

    items = sorted_items(students)
    n = min(n, len(items))

    print(f"\n🏅 Top {n}:")
    for i in range(n):
        name, score = items[i]
        print(f"{i+1}. {name} - {score:.2f} ({badge(score)})")


def stats(students: Dict[str, float]) -> None:
    if not students:
        print("📭 No students yet.")
        return

    scores = list(students.values())
    count = len(scores)
    avg = sum(scores) / count

    top_name = max(students, key=students.get)
    top_score = students[top_name]

    low_name = min(students, key=students.get)
    low_score = students[low_name]

    print("\n📊 Stats:")
    print(f"- Count: {count}")
    print(f"- Average: {avg:.2f}")
    print(f"- Highest: {top_name} - {top_score:.2f} ({badge(top_score)})")
    print(f"- Lowest:  {low_name} - {low_score:.2f} ({badge(low_score)})")


def save_to_file(students: Dict[str, float], filename: str = DATA_FILE) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved to {filename}")
    except OSError as e:
        print(f"❌ Save failed: {e}")


def load_from_file(filename: str = DATA_FILE) -> Dict[str, float]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        # ensure values are floats
        students: Dict[str, float] = {}
        for k, v in data.items():
            students[str(k)] = float(v)
        print(f"📥 Loaded from {filename}")
        return students
    except FileNotFoundError:
        print(f"📭 No save file found: {filename}")
        return {}
    except (OSError, json.JSONDecodeError, ValueError) as e:
        print(f"❌ Load failed: {e}")
        return {}


def menu() -> None:
    print("\n" + "=" * 40)
    print("Student Score Manager v2")
    print("=" * 40)
    print("1) Add/Update student score")
    print("2) Delete student")
    print("3) Query student")
    print("4) Show all (sorted)")
    print("5) Show Top N")
    print("6) Stats")
    print("7) Save")
    print("8) Load")
    print("0) Exit")
    print("=" * 40)


def main():
    students: Dict[str, float] = {}

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            add_or_update(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            query_student(students)
        elif choice == "4":
            show_all(students)
        elif choice == "5":
            show_top_n(students)
        elif choice == "6":
            stats(students)
        elif choice == "7":
            save_to_file(students)
        elif choice == "8":
            students = load_from_file()
        elif choice == "0":
            if students:
                ans = input("Save before exit? (y/n): ").strip().lower()
                if ans == "y":
                    save_to_file(students)
            print("👋 Bye!")
            break
        else:
            print("⚠️ Invalid option. Please choose again.")


if __name__ == "__main__":
    main()