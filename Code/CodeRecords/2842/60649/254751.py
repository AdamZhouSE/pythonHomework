n=int(input())
a=[-1 for i in range(n+1)]
for i in range(n):
    a[i+1]=int(input())
res=0
vis=[0 for i in range(n+1)]
def dfs(x,h):
    vis[x]=1
    if a[x]==-1:
       return h
    return dfs(a[x],h+1)
for i in range(1,n+1):
    if vis[i]==0:
        tmp=dfs(i,1)
        res=max(res,tmp)
print(res)