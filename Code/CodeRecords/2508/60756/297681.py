def dfs(x:int,visited:list,ch:list,q:int,dp:list,value:list):
    visited[x]=1
    for i in range(len(ch[x])):
        ny=ch[x][i]
        if visited[ny]==1:continue
        visited[ny]=1
        dfs(ny,visited,ch,q,dp,value)
        for j in range(q,0,-1):
            for k in range(j-1,-1,-1):
                dp[x][j]=max(dp[x][j],value[x][ny]+dp[ny][k]+dp[x][j-k-1])

n,q=map(int,input().split())
dp=[[0 for i in range(n+1)] for j in range(n+1)]
value=[[0 for i in range(n+1)] for j in range(n+1)]
visited=[0 for i in range(n+1)]
ch=[[] for i in range(n+1)]
for i in range(1,n):
    a,b,c=map(int,input().split())
    value[a][b]=c
    value[b][a]=c
    ch[a].append(b)
    ch[b].append(a)
dfs(1,visited,ch,q,dp,value)
print(dp[1][q])