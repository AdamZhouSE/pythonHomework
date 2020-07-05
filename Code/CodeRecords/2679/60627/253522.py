# 16
def fac(n):
    t = 1
    for i in range(1,n+1):
        t *= i
    return int(t)
def c(n,r):
    return int(fac(n)/(fac(r)*fac(n-r)))
def f(k):
    print('k',k)
    if k==1:
        return 3
    elif k==2:
        return 8
    elif k==3:
        return 19
    else:
        t = 3**k
        b = 0
        for i in range(2,k+1): 
            b += c(k,i)*(2**(k-i))
        print(b)
        for i in range(3,k+1): 
            b += c(k,i)*(2**(k-i))
        print(b)
        return t - b
n = int(input())
for i in range(n):
    print(f(int(input())))