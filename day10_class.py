
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "F"
    def __str__(self):
        return f"{self.name} - {self.score} ({self.get_grade()})"   
# Build a class
# s1 = Student("Tom", 85)

# print(s1.name)
# print(s1.score)
# print(s1.get_grade())

# students = [
#     Student("Tom", 90),
#     Student("Lisa", 85),
#     Student("Jack", 70)
# ]

students = []

while True:
    try:
        count = int(input("How many students? "))
        break
    except ValueError:
        print("please enter a valid number.")


for _ in range(count):
    name = input("Enter name: ")
#    score = float(input("Enter score: "))
    while True:
        try:
            score = float(input("Enter score: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    students.append(Student(name, score))

students.sort(key=lambda s: s.score, reverse=True)

print("\nTop 3:")
for s in students[:3]:
    print(s)

# for s in students:
#     print(s)

