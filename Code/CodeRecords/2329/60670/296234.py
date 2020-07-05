def union(a,b):
    global f
    fa=getf(a)
    fb=getf(b)
    if fa!=fb:
        t=f[fa]+f[fb]
        f[fa]=fb
        f[fb]=t
    return

def getf(x):
    global f
    while f[x]>=0:
        x=f[x]
    return x

def have_edge(a,b):
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            return True
    return False

a=eval(input())
n=len(a)
f=[-1 for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if have_edge(a[i],a[j]):
            union(i,j)
maxn=0
for i in range(0,n):
    maxn=max(maxn,-1*f[i])
print(maxn)