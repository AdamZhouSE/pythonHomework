from math import gcd

n = int(input())
a = int(input())
b = int(input())
c = int(input())


def uglyNumber(n, a, b, c):
    def lcm3(x, y, z):
        a = (x * y) // gcd(x, y)
        return (a * z) // gcd(a, z)

    def uglynum(x):
        return x // a + x // b + x // c - x // (a * b // gcd(a, b)) - x // (a * c // gcd(a, c)) - x // (b * c // gcd(b, c)) + x // lcm3(a, b, c)

    left = 1
    right = n * min(a, b, c)
    while left < right:
        mid = (left+right) // 2
        if uglynum(mid) < n:
            left = mid+1
        else:
            right = mid
    return left


print(uglyNumber(n, a, b, c))
