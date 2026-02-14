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

if count == 0:
    print("No students entered.")
else:
    print("\nStudent Scores:")
    for name, score in students.items():
        print(name, ":", score)

    #print(f"The Max is {max(students.values())}")
    top_student = max(students, key=students.get) #get the key of the max value
    print(f"Top student: {top_student} ({students[top_student]})")

    ave = sum(students.values())/count
    print(f"The Average is {ave:.1f}")

# students = {
#     "Tom": 90,
#     "Lisa": 85,
#     "Jack": 70,
#     "Anna": 95,
#     "Mike": 88
# }

# sorted_students = sorted(
#     students.items(),
#     key=lambda x: x[1],
#     reverse=True
# )

# print("Top 3 Students:")
# for i in range(min(3, len(sorted_students))):
#     name, score = sorted_students[i]
#     print(f"{i+1}. {name} - {score}")