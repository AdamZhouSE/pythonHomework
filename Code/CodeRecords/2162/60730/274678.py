x = float(input())
n = int(input())
if n < 0:
    n = -n
    x = float(1/x)


def half(x, n):
    if n == 0:
        return 1.0
    tmp = half(x, int(n / 2))
    if n % 2 == 0:
        return tmp * tmp
    else:
        return tmp * tmp * x


print("%.05f" % (half(x, n)))
