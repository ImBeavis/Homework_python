import random
player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")

candy = int(input("Введите кол-во конфет на столе: "))

rand_player = random.randint(1, 101)
first_move = player_1
second_move = player_2
if rand_player<50:
    first_move = player_2
    second_move = player_1
    print(f"Первый ходит {first_move}")
else:
    print(f"Первый ходит {first_move}")

print(f"На столе лежит {candy} конфет")

while candy > 29:
    pl1_hod = int(input(f"{first_move}, введите кол-во конфет, которое вы возьмете от 1 до 28: "))
    if 0<pl1_hod<29:
        candy = candy - pl1_hod
        print(f"На столе осталось {candy} конфет")
        print("----------------------------------------")
        win = second_move
        if candy < 28:
            break
    else:
        print("Переход хода за нарушение правил!")
    pl2_hod = int(input(f"{second_move}, введите кол-во конфет, которое вы возьмете от 1 до 28: "))
    if 0<pl2_hod<29:
        candy = candy - pl2_hod
        print(f"На столе осталось {candy} конфет")
        print("----------------------------------------")
        win = first_move
        if candy < 29:
            break
    else:
        print("Переход хода за нарушение правил!")
print(f"Игра окончена, выйграл игрок {win}!!!")