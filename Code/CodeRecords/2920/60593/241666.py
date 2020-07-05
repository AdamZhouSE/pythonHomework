n,k=map(int,input().split())
a=list(map(int,input().split()))
suf=[0]*(n+1)
for i in range(n-1,-1,-1):
    suf[i]=suf[i+1]+a[i]
ans=suf[0]
aft=[0]
aft.extend(sorted(suf[1:]))
for i in range(n-1,n-k+1,-1):
    ans-=aft[i]
print(ans)