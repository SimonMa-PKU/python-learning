import json
import os

# students = {
#     "Tom": 90,
#     "Lisa": 85,
#     "Jack": 70
# }

# with open("students.json", "w", encoding = "utf-8") as file:
#     json.dump(students, file, ensure_ascii=False, indent=4)

# print("Saved to JSON.")

# with open("students.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# print("Loaded data:")
# print(data)

# 1. Load existing data if file exists
if os.path.exists("students.json"):
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            students = json.load(file)
        print("Loaded existing data.")
    except json.JSONDecodeError:
        print("⚠ JSON file corrupted. Starting fresh.")
        students = {}

else:
    students = {}
    print("No existing file. Starting new.")

# 2. Add new student
while True:
    try:
        count = int(input("How many students? "))
        break
    except ValueError:
        print("please enter a valid number.")

for _ in range(count):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    students[name] = score

# 3. Save back to JSON
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

print("Saved successfully.")

# 4.Read and print JSON
with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("Loaded data:", loaded_students)
