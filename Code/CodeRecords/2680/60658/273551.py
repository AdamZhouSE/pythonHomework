def fac(x):
    if f[x]!=0:
        return f[x]
    f[x]=x*fac(x-1)
    return f[x]

def combination(m,n):
    return fac(n)//(fac(m)*fac(n-m))


f = [0 for i in range(100)]
f[0]=f[1]=1
t = int(input())
for i in range(t):
    n,m = [int(x) for x in input().split()]  
    print(combination(n-1,m+n-2))