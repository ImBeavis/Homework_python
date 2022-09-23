N = int(input("Введите число: "))

if (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0:
    print(f"{N} - кратно")  
else:
    print(f"{N} - не кратно!")