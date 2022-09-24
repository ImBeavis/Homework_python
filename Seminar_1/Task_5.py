X = int(input("Введите координату X: "))
Y = int(input("Введите координату Y: "))
Z = int(input("Введите координату Z: "))

formula_1 = not(X or Y or Z)
formula_2 = not X and not Y and not Z
result = formula_1 == formula_2

if result == True:
    print("Утверждение верно")
else:
    print("Утверждение не верно")