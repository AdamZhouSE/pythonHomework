n,k=map(int,input().split())
a=list(map(int,input().split()))
d=[0]*n
for i in range(n-1):
    d[i]=a[i+1]-a[i]
d.sort()
ans=a[n-1]-a[0]
pr=n-2
for i in range(k):
    ans-=d[pr]
    pr-=1
print(ans)
