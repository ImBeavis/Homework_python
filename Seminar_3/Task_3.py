import random

size_list = int(input("Задайте размера списка: "))
number = float(input("Задайте размер чисел списка: "))

my_list = []

for i in range(size_list):
    my_list.append(round(random.uniform(0, number), 2))

print(my_list)

max_number = my_list[0] - int(my_list[0])
min_number = my_list[0] - int(my_list[0])
for i in my_list:
    i = i - int(i)
    if i != 0 and i > max_number:
        max_number = i
    if i != 0 and i < min_number:
        min_number = i

print(f"Максимальная дробная часть: {round(max_number, 2)}")
print(f"Минимальаня дробная часть :{round(min_number, 2)}")

print(f"Их разница: {round(max_number - min_number, 2)}")