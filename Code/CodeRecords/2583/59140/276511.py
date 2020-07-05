import math
from numpy import long


def Lcm(x, y, z):
    a = (x * y) // math.gcd(x, y)
    return (a * z) // math.gcd(a, z)


def uglynum(x):
    return x // a + x // b + x // c - x // (a * b // math.gcd(a, b)) - x // (a * c // math.gcd(a, c)) - x // (
            b * c // math.gcd(b, c)) + x // Lcm(a, b, c)

n=long(input())
a=long(input())
b=long(input())
c=long(input())
left = 1
right = n * min(a, b, c)
while left < right:
    mid = (left + right) // 2
    if uglynum(mid) < n:
        left = mid + 1
    else:
        right = mid
print(left)