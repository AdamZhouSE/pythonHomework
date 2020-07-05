from math import sqrt
def digitsum(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum
def factoring(n):
    primes=[i for i in range(2,n) if 0 not in [i%d for d in range(2,int(sqrt(i))+1)]]
    result=[]
    for p in primes:
        while n!=1:
            if n%p==0:
                n = n // p
                result.append(p)
            else:break
    if len(result)<=1:return -1
    sum=0
    for i in result:
        sum+=digitsum(i)
    return sum


t=int(input())
for _ in range(t):
    n=int(input())
    sum=digitsum(n)
    factorsum=factoring(n)
    if sum==factorsum:print(1)
    else:print(0)