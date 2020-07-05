def myPow(x, n):
    if (n == 0):
        return 1.0
    if (n < 0):
        x = 1 / x
    n = abs(n)
    x0 = x * x
    return myPow(x0, n // 2) if (n % 2 == 0) else x * myPow(x0, n // 2)


x = float(input())
n = int(input())
print(format(myPow(x, n), '.5f'))