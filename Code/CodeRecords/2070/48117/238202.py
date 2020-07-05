x = float(input())
n = int(input())
if n == 0:
    print(1.0)
else:
    if n < 0:
        xCopy = 1 / x
        x = 1 / x
        n = -n
    else:
        xCopy = x
while n > 1:
    x *= xCopy
    n -= 1

print('%.5f'%x)