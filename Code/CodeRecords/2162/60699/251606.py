x=float(input())
n=int(input())


def __help(a, b):
    if b == 1:
        return a
    elif b & 1:
        return a * __help(a, b - 1)
    elif not b & 1:
        return __help(a * a, b // 2)


if n > 0:
    print(__help(x, n)) 
elif n == 0:
    print(1) 
else:
    print(__help(1 / x, -n)) 