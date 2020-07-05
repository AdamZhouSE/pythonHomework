import collections

def factorial(x):
    if fac[x]!=0:
        return fac[x]
    if x==0 or x==1:
        return 1
    fac[x]=x*factorial(x-1)
    return fac[x]

t = int(input())
fac = [0 for i in range(100)]
for i in range(t):
    N,M,l,r = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    dic = dict(collections.Counter(arr))
    pool = {}
    for i in range(l,r+1):
        if i in dic:
            pool[i]=dic[i]
        else:
            pool[i]=0
    for i in range(M):
        min_ = min(pool,key=pool.get)
        pool[min_]+=1
    dic.update(pool)
    denominator = 1
    for i in dic.values():
        denominator*=factorial(i)
    numerator = factorial(N+M)
    print((numerator//denominator)%998244353)