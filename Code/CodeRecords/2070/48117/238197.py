x = float(input())
n = int(input())
xCopy = x
if n == 0:
    print(1.0)
else:
    if n < 0:
        x = 1 / x
        n = -n
while n > 1:
    x *= xCopy
    n -= 1

print('%.5f'%x)