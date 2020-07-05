def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

n=int(input())
if n<=2:
    print(0)
else:
    c=0
    for i in range(2, n):
        if isPrime(i):
            c=c+1
    print(c)