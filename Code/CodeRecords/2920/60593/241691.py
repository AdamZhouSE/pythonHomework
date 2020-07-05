n,k=map(int,input().split())
a=list(map(int,input().split()))
be=-1
ans=0
for i in range(n):
    if(be==-1):
        be=a[i]
        a[i]=0
    else:
        a[i]-=be
        be+=a[i]
    ans+=a[i]
a.sort()
for i in range(n-1,-1,-1):
    if(k==1):
        break
    else:
        k-=1
        ans-=a[i]
print(ans)