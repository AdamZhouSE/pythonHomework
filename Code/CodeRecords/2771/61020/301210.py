import math


def is_square(n):
    r = int(math.floor(math.sqrt(n)))

    return r * r == n


T = int(input())
for i in range(T):
    if is_square(int(input())):
        print(1)
    else:
        print(0)
