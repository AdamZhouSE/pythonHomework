from math import sqrt


def is_prime(a):
    flag = True
    for k in range(2, int(sqrt(a))):
        if a % k == 0:
            flag = False
    return flag


n = int(input())
for i in range(0, n):
    m = int(input())
    j = 2
    factor = []
    while j <= m:
        if is_prime(j) and m % j == 0:
            factor.append(j)
            m = m // j
        else:
            j += 1
    if len(factor) == 3 and len(factor) == len(set(factor)):
        print(1)
    else:
        print(0)
