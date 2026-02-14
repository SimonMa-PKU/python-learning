# student = {
#     "name": "Simon",
#     "age": 18,
#     "major": "Computer Science"
# }

# print(student)
# print(student["name"])
# print(student["age"])

# student["age"] = 19
# student["gpa"] = 3.8
# print(student)

# for key in student:
#     print(key, ":", student[key])

# for key, value in student.items():
#     print(key, ":", value)

count = int(input("How many students? "))

students = {}

for _ in range(count):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    students[name] = score

print("\nStudent Scores:")
for name, score in students.items():
    print(name, ":", score)

print(f"The Max is {max(students.values())}")
ave = sum(students.values())/count
print(f"The Average is {ave:.2f}")
