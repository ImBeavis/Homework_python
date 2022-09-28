number = int(input("Введите размер списка: "))
workList = []

for i in range(1, number+1):
    workList.append(float((1+1/i)**i))

print(workList)

Sum_number = 0
for i in workList:
    Sum_number = i+Sum_number
print(round(Sum_number, 2))