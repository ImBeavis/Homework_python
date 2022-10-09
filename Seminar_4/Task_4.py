from random import randint
import itertools

k = int(input("Введите степень: "))

def get_degree(k):
    degree = [randint(-100, 100) for i in range (k + 1)]
    while degree[0] == 0:
        degree[0] = randint(1, 10) 
    return degree

def get_polynomial(k, degree):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(degree, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


degree = get_degree(k)
polynom1 = get_polynomial(k, degree)
print(polynom1)

with open('text.txt', 'w') as data:
    data.write(polynom1)

k = int(input("Введите степень второго многочлена: "))

ratios = get_degree(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('text2.txt', 'w') as data:
    data.write(polynom2)