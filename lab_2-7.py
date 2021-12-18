import math
from random import randint

n = 1

num_list = [randint(-100,100) for i in range(10+n)]

def abs_for_list(ls):
    ls = list(ls)
    result = []
    for i in ls:
        result.append(abs(i))
    return result

print("new list:       ", num_list)
print("list after abs: ", abs_for_list(num_list))