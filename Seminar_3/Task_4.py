number = int(input("Введите число: "))
res = ""
while number > 0:
    res = str(number % 2) + res
    number = number // 2

print(res)