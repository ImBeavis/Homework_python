import random

size_list = int(input("Задайте размера списка: "))
number = int(input("Задайте размера чисел списка: "))

my_list = []

for i in range(size_list):
    my_list.append(random.randrange(0, number))

print(my_list)

result= 0
k = 1
if len(my_list) % 2 == 0:
    for i in range(len(my_list) // 2):
        result = my_list[i] * my_list [-k]
        k = k+1
        print(result)
else:
    for i in range((len(my_list) // 2)+1):
        result = my_list[i] * my_list [-k]
        k = k+1
        print(result)