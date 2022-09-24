from base64 import b16decode


a = []
for i in range(2):
    a.append(int(input("Введите координату точки А: ")))

b = []
for i in range(2):
    b.append(int(input("Введите координату точки B: ")))

result = (((b[0] - a[0])**2) + ((b[1] - a[1])**2))**0.5
print(round(result, 2))