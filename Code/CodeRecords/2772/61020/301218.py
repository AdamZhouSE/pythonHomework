import math


def cbrt(n):
    return int(math.floor(pow(n, 1 / 3)))


T = int(input())
for i in range(T):
    print(cbrt(i))
