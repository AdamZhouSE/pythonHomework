def dfs(u,k):
    if(visited[u]):return False
    if(k==t-1):return True
    ans[k]=u&1
    visited[u]=True
    if(dfs((u<<1)&(t-1),k+1)):return True
    if(dfs((u<<1|1)&(t-1),k+1)):return True
    visited[u]=False
    return False

n = int(input())
t = 2**n
print(t,end=" ")
ans = [0 for i in range(t)]
visited = [False for i in range(t)]
dfs(0,0)
ans = [str(i) for i in ([0]*(n-1)+ans)[:t]]
print("".join(ans))