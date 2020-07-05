x = float(input())
n = int(input())
if n < 0:
    x = 1 / x
    n = -n
pow = 1
while n:
    if n & 1:
        pow *= x
    x *= x
    n >>= 1
print(format(pow,'.5f'))