n=int(input())
k=list(map(int,input().split()))
ans=0
s=sum(k)
if s%3==0:
    p=s//3
    v=s-p
    s=t=0
    for i in range(n-1):
        s+=k[i]
        if s==v: ans+=t
        if s==p: t+=1
print(ans)