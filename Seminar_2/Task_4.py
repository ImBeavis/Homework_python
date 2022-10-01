my_list = [1,2,3,4,5,6,7,8,9,10]
import random
random_list = []

for i in range(0, len(my_list)):
    k = random.randrange(0, len(my_list))
    random_list.append(my_list[k])
    my_list.remove(my_list[k])
print(random_list)