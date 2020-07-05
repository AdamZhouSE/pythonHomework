def mypow(x, n):
    if n < 0:
        return 1 / mypow_dd(x, -n)
    else:
        return mypow_dd(x, n)


def mypow_dd(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        temp = mypow_dd(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp


a = float(input())
b = float(input())
print(format(mypow(a, b),'.5f'))