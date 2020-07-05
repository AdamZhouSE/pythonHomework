import math


def jc(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
k = int(input())
res = ""
while n > 0:
    temp = jc(n - 1)
    index = int(math.ceil(k / temp))-1
    if index<0:
        index = 0
    res += str(l.pop(index))
    k %= temp
    n -= 1
print(res)