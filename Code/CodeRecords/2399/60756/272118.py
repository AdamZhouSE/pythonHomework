from collections import defaultdict
def fac(x:int)->int:
    s=1
    for i in range(1,x+1):
        s*=i
    return s

T=int(input())
for t in range(T):
    d=defaultdict(int)
    n,m,l,r=tuple(map(int,input().split()))
    arr=list(map(int,input().split()))
    ans=fac(n+m)
    for i in arr:
        d[i]+=1
    for i in range(l, r + 1):
        if m > 0 and i not in d:
            d[i] += 1
            m-=1
        else:
            d[i]=d[i]
    while m>0:
        d[min(d,key=lambda x:d[x] if l<=x<=r else float("Inf"))]+=1
        m-=1
    for value in d.values():
        ans//=fac(value)
    print(ans)