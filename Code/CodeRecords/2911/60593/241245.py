def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
n,m=map(int,input().split())
cost=list(map(int,input().split()))
fa=list(range(n+1))
for i in range(m):
    x,y=map(int,input().split())
    fx=find(x)
    fy=find(y)
    if(fx!=fy):
        fa[fx]=fy
S=[]
for i in range(1,n+1):
    S.append((find(fa[i]),cost[i-1]))
S.sort(key=lambda x:(x[0],x[1]))
f=-1
ans=0
for i in S:
    if(i[0]!=f):
        ans+=i[1]
        f=i[0]
print(ans)

    
