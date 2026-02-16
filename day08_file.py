# with open("test.txt", "w") as file:
#     file.write("Hello Day 8!\n")
#     file.write("Learning file I/O.\n")

# print("File written.")

# with open("test.txt", "r") as file:
#     content = file.read()

# print("File content:")
# print(content)

# students = {
#     "Tom": 90,
#     "Lisa": 85,
#     "Jack": 70
# }

# with open("students.txt", "w") as file:
#     for name, score in students.items():
#         file.write(f"{name},{score}\n")

# print("Saved successfully.")

# students = {}

# with open("students.txt", "r") as file:
#     for line in file:
#         name, score = line.strip().split(",")
#         students[name] = float(score)

# print(students)


def save_students(students):
    with open("students.txt", "w") as file:
        for name, score in students.items():
            file.write(f"{name},{score}\n")

def load_students():
    students = {}
    with open("students.txt", "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            students[name] = float(score)
    return students

count = int(input("How many students? "))

if count <= 0:
    print("No students entered.")

students = {}


for _ in range(count):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    students[name] = score

print("Saving to file...")

# with open("students.txt", "w") as file:
#     for name, score in students.items():
#         file.write(f"{name},{score}\n")

save_students(students)

grades = {}

print("Loading from file...")

# with open("students.txt", "r") as file:
#     for line in file:
#         name, score = line.strip().split(",")
#         grades[name] = float(score)

grades = load_students()

print(grades)

