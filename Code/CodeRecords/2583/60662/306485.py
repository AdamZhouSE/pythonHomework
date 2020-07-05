def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm2(x, y):
    return x * y // gcd(x, y)


def lcm3(x, y, z):
    rs = lcm2(x, y)
    return lcm2(z, rs)


def cnt(k, x, y, z):
    return k // x + k // y + k // z - k // lcm2(x, y) - k // lcm2(x, z) - k // lcm2(y, z) + k // lcm3(x, y, z)


n = int(input())
a = int(input())
b = int(input())
c = int(input())
f = min([a, b, c])
r = 2 * 10 ** 9
# 二分法
while f < r:
    mid = (f + r) >> 1
    if cnt(mid, a, b, c) < n:
        f = mid + 1
    else:
        r = mid
print(f)


