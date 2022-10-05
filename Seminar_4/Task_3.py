size_list = int(input("Введите размер последовательности чисел: "))
number_set = []

for i in range(size_list):
    number_set.append(int(input("Введите число: ")))

print(number_set)

result_number = []
for i in number_set:
    if number_set.count(i) == 1:
        result_number.append(i)

print(result_number)






