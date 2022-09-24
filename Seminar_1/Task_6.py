X = int(input("Введите координату X: "))
Y = int(input("Введите координату Y: "))

if X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print(f"X = {X}, Y = {Y} - во второй четверти")
    if X > 0 and Y < 0:
        print(f"X = {X}, Y = {Y} - в четвёртой четверти")
    if X < 0 and Y < 0:
        print(f"X = {X}, Y = {Y} - в третьей четверти")
    if X < 0 and Y > 0:
        print(f"X = {X}, Y = {Y} - в первой четверти")
else:
    print("Координата находится в центре графика!")
