n,k=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
d=[0]*(n+1)
for i in range(n):
    d[i]=a[i+1]-a[i]
d.sort()
ans=a[n-1]-a[0]
pr=n-2
for i in range(k-1):
    ans-=d[pr]
    pr-=1
print(ans)
