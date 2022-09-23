N = int(input("Введите число: "))

if 1 <= N <= 7:
    if N == 6 or N == 7:
        print(f"{N} - Выходной")
    else:print(f"{N} - Будни")
else:
    print("Нет такого дня недели!")