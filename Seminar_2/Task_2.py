number = int(input("Введите число: "))
kit_work = []
factorial = 1
 
for i in range(1, number+1):
    factorial *= i
    kit_work.insert(i, factorial)

print(f"N = {number} тогда, {kit_work}")