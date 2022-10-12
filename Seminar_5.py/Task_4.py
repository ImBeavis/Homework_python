# Кодинг RLE

RLE_read = r"RLEtext1.txt"

with open (RLE_read) as data:
    file = data.read()
print(file)

c = list(set(file))

for i in c:
    print(file.count(i), end = "")
    print(i, end = "")