
# userInput = int(input("Введите число N: "))
# print("Результат:", end = " ")

# if userInput < 0: multiplier = -1
# else: multiplier = 1

# for i in range(-userInput, userInput + multiplier, multiplier):
#     if i * multiplier < userInput * multiplier:
#         print(i, end = ", ")
#     else:
#         print(i)


import math
userInput = int(input("Введите число N: "))
result = [int(math.copysign(1, userInput)) * i for i in range (-abs(userInput), abs(userInput) + 1)]
print(f"Результат: {result}")