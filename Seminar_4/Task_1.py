import math

number = int(input("Введите число знаков после запятой числа пи: "))
if  1000000000 > number > 0:
    print(round(math.pi, number))
else:
    print("Введите корректное число!")
