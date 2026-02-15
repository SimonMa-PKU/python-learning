# def greet():
#     print("Hello, welcome to Day 7!")

# greet()

# def greet(name):
#     print(f"Hello {name}!")

# greet("Simon")
# greet("Tom")

# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

count = int(input("How many scores?"))

for _ in range(count):
    score = int(input("Enter score: "))
    grade = calculate_grade(score)
    print(f"Score: {score} -> Grade: {grade}")



# while True:
#     try:
#         score = int(input("Enter score: "))
#         break
#     except ValueError:
#         print("Please enter a valid number.")

# print(f"Grade: {calculate_grade(score)}")

# score = int(input("Enter score: "))
# print(calculate_grade(score))


# print(calculate_grade(95))
# print(calculate_grade(75))
