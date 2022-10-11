string = "ывапыв фывацабвыыкр аыфвпвыа цевбауе "
print(string)
string = string.split()

search = input("Введите элемент слова, которое нужно удалить: ")

for i in range(len(string)):
    if search not in string[i]:
        print(string[i], end = " ")