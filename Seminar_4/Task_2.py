number = int(input("Введите натуральное число: "))

result = []

while number > 0:
    if number % 2 == 0:
        number = number / 2
        result.append(2)
    elif number % 3 == 0:
        number = number / 3
        result.append(3)
    else:
        result.append(int(number))
        break

print(result)