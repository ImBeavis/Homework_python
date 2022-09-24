quarter = int(input("Введите номер четверти: "))

if quarter > 0 and quarter < 5:
    if quarter == 1:
        print("Возможные координаты: X < 0 и Y > 0")
    if quarter == 2:
        print("Возможные координаты: X > 0 и Y > 0")
    if quarter == 3:
        print("Возможные координаты: X < 0 и Y < 0")
    if quarter == 4:
        print("Возможные координаты: X > 0 и Y < 0") 
else:
    print("Нет такой четверти!")