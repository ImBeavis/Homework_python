N = float(input("Введите дробное число: "))

result = int( (N*10) % 10 )

if result != 0:
    print(result)
    
else: print("Нет")