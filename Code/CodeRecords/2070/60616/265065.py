def myPow(x, n) :
    if n < 0:
        x = 1 / x
        n = -n

    res = 1
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

x=float(input())
n=int(input())
print('%.5f' % myPow(x,n))