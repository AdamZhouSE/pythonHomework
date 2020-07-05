x = eval(input())
n = int(input())
if n < 0:
    n = -n
    x = 1 / x


def half(x, n):
    if n == 0:
        return 1.0
    tmp = half(x, int(n / 2))
    if n % 2 == 0:
        return tmp * tmp
    else:
        return tmp * tmp * x


print(half(x, n))
