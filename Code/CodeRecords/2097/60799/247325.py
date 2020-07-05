import math

a, b = int(input()), int(input())
g = math.gcd(a, b)
a, b = int(a / g), int(b / g)
g = b
while True:
    if g % 2 == 0:
        g = int(g / 2)
    elif g % 5 == 0:
        g = int(g / 5)
    else:
        break
if g == 1:
    print('{:g}'.format(a / b))
else:
    d = {}
    INT = str(int(a / b))
    k = (a % b)
    index = 0
    while True:
        if k in d:
            index = list(d.keys()).index(k)
            d = [str(i) for i in list(d.values())]
            break
        else:
            d[k] = int(10 * k / b)
            k = (10 * k % b)
            index += 1
    print(INT + '.' + ''.join(d[0:index]), end='')
    if index < len(d):
        print('('+''.join(d[index:])+')')