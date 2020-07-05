from math import  gcd
# 三数最小公倍数=两数最小公倍数与第三个数的最小公倍数
def Lcm(x, y, z):
    a = (x * y) // gcd(x, y)
    return (a * z) // gcd(a, z)
def uglynum(x):
    return x // a + x // b + x // c - x // (a * b // gcd(a, b)) - x // (a * c // gcd(a, c)) - x // (b * c // gcd(b, c)) + x // Lcm(a, b, c)
n=int(input())
a=int(input())
b=int(input())
c=int(input())
left = 1
right = n * min(a, b, c)
while left < right:
    mid = (left + right) // 2
    if uglynum(mid) < n:
        left = mid + 1
    else:
        right = mid
print (left)