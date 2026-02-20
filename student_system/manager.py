import json
import os
from .student import Student

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, score):
        self.students.append(Student(name, score))
    
    def show_all(self):
        for s in self.students:
            print(s)

    def save(self, filename):
        filename = str(filename)
        data = [s.to_dict() for s in self.students]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    
    def load(self, filename):
        filename = str(filename)
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
#        self.students = [Student.from_dict(d) for d in data]
        # ✅ 情况1：data 是 dict：{"Tom": 90, ...}
        if isinstance(data, dict):
            self.students = [Student(name, score) for name, score in data.items()]
            return

        # ✅ 情况2：data 是 list：[{"name": "...", "score": ...}, ...]
        if isinstance(data, list):
            self.students = [Student.from_dict(d) for d in data]
            return

        raise ValueError("Unsupported JSON format for students.json")