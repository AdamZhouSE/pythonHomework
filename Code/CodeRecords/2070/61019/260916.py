x = eval(input())
n = eval(input())
res = 1
if n < 0:
    x = 1 / x
    res = x
    n = -n - 1

base = x
while n > 0:
    res *= base if n % 2 == 1 else 1
    base *= base
    n //= 2

print('{:.5f}'.format(res))
