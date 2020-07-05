import math


def numSqures(n):
    while n % 4 == 0:
        n = int(n / 4)
    if n % 8 == 7:
        return 4
    a = 0
    while a * a <= n:
        b = int(math.sqrt(n - a * a))
        if a * a + b * b == n:
            if a != 0 and b != 0:
                return 2
            else:
                return 1
        a += 1
    return 3


n = int(input())
print(str(numSqures(n)))
