# Декодинг RLE

RLE_read_2 = r"RLEtext2.txt"

with open (RLE_read_2) as data:
    file = data.read()
print(file)

unZip = ''
zip =''
for i in file:
    if i.isdigit():
        zip = zip + i
    else:
        unZip += str(int(zip) * i)
        zip = ''

print(unZip)