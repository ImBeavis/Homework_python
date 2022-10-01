import random

size_list = int(input("Задайте размера списка: "))
number = int(input("Задайте размера чисел списка: "))

my_list = []

for i in range(size_list):
    my_list.append(random.randrange(0, number))

print(my_list)

sum_elem = 0
for i in range(len(my_list)):
    if i % 2 == 1:
        sum_elem = sum_elem+my_list[i]

print(sum_elem)