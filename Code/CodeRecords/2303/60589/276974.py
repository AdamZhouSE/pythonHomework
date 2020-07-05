n=int(input())
m=2**n
vis=[0]*(m)
ans=[0]*(m)


def dfs(x,k):
    if vis[x]:
        return 0
    if k==m:
        return 1
    vis[x]=1
    ans[k]=x&1
    if dfs((x << 1) & (m - 1), k + 1):
        return 1
    if dfs((x << 1 | 1) & (m - 1), k + 1):
        return 1
    vis[x]=0
    return 0


res=str(m)+' '
dfs(0,1)
for i in range(n-1):
    res=res+'0'
for i in range(1,m-n+2):
    res=res+str(ans[i])
print(res)