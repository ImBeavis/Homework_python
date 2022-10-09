import re
import itertools


file1 = 'text.txt'
file2 = 'text2.txt'
file_sum = 'sum_text.txt'

def read_file(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def convert_file(polinom):
    polinom = polinom.replace('= 0', '')
    polinom = re.sub("[*|^| ]", " ", polinom).split('+')
    polinom = [char.split(' ') for char in polinom]
    polinom = [[x for x in list if x] for list in polinom]
    for i in polinom:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    polinom = [tuple(int(x) for x in j if x != 'x') for j in polinom]
    return polinom

def fold_pols(polinom_1, polinom_2):   
    x = [0] * (max(polinom_1[0][1], polinom_2[0][1] + 1))
    for i in polinom_1 + polinom_2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

def get_sum_pol(polinom):
    var = ['*x^'] * len(polinom)
    coefs = [x[0] for x in polinom]
    degrees = [x[1] for x in polinom]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, polinom):
    with open(file, 'w') as data:
        data.write(polinom)

pol1 = read_file(file1)
pol2 = read_file(file2)
pol_1 = convert_file(pol1)
pol_2 = convert_file(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)