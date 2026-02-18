import json
import os
from typing import List, Optional


class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def get_grade(self) -> str:
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "F"

    def __str__(self) -> str:
        return f"{self.name:<15} {self.score:>6.2f}  Grade: {self.get_grade()}"

    def to_dict(self) -> dict:
        return {"name": self.name, "score": self.score}

    @staticmethod
    def from_dict(data: dict) -> "Student":
        return Student(str(data["name"]), float(data["score"]))


class StudentManager:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, score: float) -> None:
        # if name exists, update score; else add new
        existing = self.find_student(name)
        if existing:
            existing.score = score
            print(f"✅ Updated: {name} -> {score}")
        else:
            self.students.append(Student(name, score))
            print(f"✅ Added: {name} -> {score}")

    def delete_student(self, name: str) -> bool:
        s = self.find_student(name)
        if not s:
            return False
        self.students.remove(s)
        return True

    def find_student(self, name: str) -> Optional[Student]:
        for s in self.students:
            if s.name == name:
                return s
        return None

    def show_all(self) -> None:
        if not self.students:
            print("📭 No students.")
            return

        # sort by score desc, then name asc
        items = sorted(self.students, key=lambda s: (-s.score, s.name))

        print("\n📋 Students (sorted):")
        for i, s in enumerate(items, start=1):
            print(f"{i:>2}. {s}")

    def top_n(self, n: int) -> List[Student]:
        if n <= 0:
            return []
        items = sorted(self.students, key=lambda s: s.score, reverse=True)
        return items[: min(n, len(items))]

    def stats(self) -> None:
        if not self.students:
            print("📭 No students.")
            return

        scores = [s.score for s in self.students]
        avg = sum(scores) / len(scores)

        top_student = max(self.students, key=lambda s: s.score)
        low_student = min(self.students, key=lambda s: s.score)

        print("\n📊 Stats:")
        print(f"- Count: {len(self.students)}")
        print(f"- Average: {avg:.2f}")
        print(f"- Highest: {top_student.name} - {top_student.score:.2f} ({top_student.get_grade()})")
        print(f"- Lowest:  {low_student.name} - {low_student.score:.2f} ({low_student.get_grade()})")

    def save(self, filename: str) -> None:
        data = [s.to_dict() for s in self.students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved to {filename}")

    def load(self, filename: str) -> None:
        if not os.path.exists(filename):
            print(f"📭 No file found: {filename}")
            self.students = []
            return

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = [Student.from_dict(item) for item in data]
            print(f"📥 Loaded from {filename}")
        except json.JSONDecodeError:
            print("⚠ JSON corrupted. Start with empty list.")
            self.students = []


def input_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("⚠ Please enter an integer.")


def input_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠ Please enter a number.")


def input_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("⚠ Cannot be empty.")


def menu():
    print("\n" + "=" * 40)
    print("Student Manager (OOP)")
    print("=" * 40)
    print("1) Add/Update student")
    print("2) Delete student")
    print("3) Show all")
    print("4) Show Top N")
    print("5) Stats")
    print("6) Save")
    print("7) Load")
    print("0) Exit")
    print("=" * 40)


def main():
    manager = StudentManager()
    filename = "students_oop.json"

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input_nonempty("Enter name: ")
            score = input_float("Enter score: ")
            manager.add_student(name, score)

        elif choice == "2":
            name = input_nonempty("Enter name to delete: ")
            ok = manager.delete_student(name)
            print("🗑 Deleted." if ok else "❌ Not found.")

        elif choice == "3":
            manager.show_all()

        elif choice == "4":
            n = input_int("Top N = ")
            top_list = manager.top_n(n)
            print(f"\n🏅 Top {min(n, len(top_list))}:")
            for i, s in enumerate(top_list, start=1):
                print(f"{i}. {s}")

        elif choice == "5":
            manager.stats()

        elif choice == "6":
            manager.save(filename)

        elif choice == "7":
            manager.load(filename)

        elif choice == "0":
            print("👋 Bye!")
            break

        else:
            print("⚠ Invalid option.")


if __name__ == "__main__":
    main()
