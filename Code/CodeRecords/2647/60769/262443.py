import math


def isSqrt(n):
    temp = int(math.sqrt(n))
    return temp * temp == n


def solve(n):
    if isSqrt(n):
        return 1
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4
    for i in range(int(math.sqrt(n)) + 1):
        if isSqrt(n - i * i):
            return 2
    return 3


num = int(input())
for j in range(num):
    nn = int(input())
    print(solve(nn))