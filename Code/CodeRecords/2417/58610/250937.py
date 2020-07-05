from math import gcd
a: list = eval(input())
res = a[0]
for num in a:
    res = gcd(res, num)
print(res == 1)