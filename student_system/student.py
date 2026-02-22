class Student:
    def __init__(self, name:str, score:float):
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

    def to_dict(self) -> dict:
        return {"name": self.name, "score": self.score}
    
    @staticmethod
    def from_dict(data: dict):
        return Student(data["name"], data["score"])
    
    def __str__(self):
        return f"{self.name} - {self.score} ({self.get_grade()})"
