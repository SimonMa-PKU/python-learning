import json
import os
from .student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def find_student(self, name: str):
        for s in self.students:
            if s.name == name:
                return s
        return None

    def add_student(self, name: str, score: float) -> None:
        existing = self.find_student(name)
        if existing:
            existing.score = float(score)  # update
        else:
            self.students.append(Student(name, float(score)))

    def delete_student(self, name: str) -> bool:
        s = self.find_student(name)
        if not s:
            return False
        self.students.remove(s)
        return True

    def top_n(self, n: int):
        if n <= 0:
            return []
        items = sorted(self.students, key=lambda s: s.score, reverse=True)
        return items[: min(n, len(items))]

    def save(self, filename) -> None:
        filename = str(filename)
        data = {s.name: s.score for s in self.students}  # 你当前 JSON 是 dict 格式
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self, filename) -> None:
        filename = str(filename)
        if not os.path.exists(filename):
            self.students = []
            return

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 兼容 dict 格式：{"Tom": 90, ...}
        if isinstance(data, dict):
            self.students = [Student(name, float(score)) for name, score in data.items()]
            return

        # 兼容 list 格式：[{"name": "...", "score": ...}, ...]
        if isinstance(data, list):
            self.students = [Student.from_dict(d) for d in data]
            return

        raise ValueError("Unsupported JSON format")