def myPow( x, n):
    if n == 0:
        return 1
    elif n < 0:
        x = 1/x
        n = -n
    ans = 1.0
    while n > 0:
        if n&1 :
            ans *= x
        x *= x
        n >>= 1
    return ans
x=float(input());
n=int(input());
print('%.5f'%myPow(x,n))