# 插空法
from math import factorial
def res_given_num_of_1(n,i):
    space = n-i+1
    if space<i:
        return 0
    return factorial(space)//factorial(i)//factorial(space-i)#c(space,i)

t = int(input())
for k in range(t):
    n = int(input())
    res = 0
    for i in range(n):
        res += res_given_num_of_1(n,i)
    print(res)