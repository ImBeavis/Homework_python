number = float(input("Введите число: "))
number = str(number)
number = list(number)
sum = 0

for i in number:
    if i != ".":
        sum = sum + int(i)

print(sum)