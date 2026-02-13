# numbers = [10, 20, 30]

# # print(numbers)
# # print(numbers[0])
# # print(numbers[1])
# # print(numbers[2])

# for num in numbers:
#     print(num)

# numbers = []

# numbers.append(5)
# numbers.append(10)
# numbers.append(15)

# print(numbers)

count = int(input("How many numbers? "))
if count <= 0:
    print("Please enter a positive number.")
else:
    numbers = []

    for _ in range(count):
        num = float(input("Enter number: "))
        numbers.append(num)

    total = sum(numbers)

    print(f"Numbers: {numbers}")
    print(f"Total is {total:.2f}")
    print(f"The max is {max(numbers)}")
    print(f"The min is {min(numbers)}")
