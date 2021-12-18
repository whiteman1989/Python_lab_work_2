import math
from random import randint

n = 1

num_list = [randint(-100,100) for i in range(10+n)]

m = randint(1,100)

def filter_lis(m, ls):
    ls = list(ls)
    result = []
    for i in ls:
        if(math.fabs(i) > m):
            result.append(i)
    return result

print("M = ", m)
print("new list:      S", num_list)
print("filtered list: ", filter_lis(m, num_list))