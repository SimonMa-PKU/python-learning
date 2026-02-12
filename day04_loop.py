# total = 0
# for i in range(1, 6):
#     total = total + i

# print("Total is:", total)

# secret = 7
# guess = 0

# while guess != secret:
#     guess = int(input("Guess the numeber: ") )
# print("You got it!")

total = 0
number = 0

for _ in range(3):
    number = float(input("Enter number: "))
    total += number

print(f"Total is: {total:.2f}")