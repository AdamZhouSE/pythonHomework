class Path:
    def __init__(self):
        self.nxt,self.ends=0,0
def dfs(u,fa):
    sz[u],dp[u][0],dp[u][1]=1,1,1
    p=pta[u]
    while(p):
        v=ph[p].ends
        if(v!=fa):
            dfs(v,u)
            sz[u]+=sz[v]
            for j in range(sz[u],-1,-1):
                for k in range(min(j,sz[u]-sz[v]),max(1,j-sz[v])-1,-1):
                    dp[u][j]=max(dp[u][j],dp[u][k]*dp[v][j-k])
        p=ph[p].nxt
    for i in range(1,sz[u]+1):
        dp[u][0]=max(dp[u][0],dp[u][i]*i)
def makep(u,v):
    global e
    e+=1
    ph[e].ends=v
    ph[e].nxt=pta[u]
    pta[u]=e
n=int(input())
e=0
ph=[Path() for i in range(1500)]
pta,sz,dp=[0]*1500,[0]*1500,[[0]*1500 for i in range(1500)]
for i in range(n-1):
    x,y=map(int,input().split())
    makep(x,y)
    makep(y,x)
dfs(1,1)
print(dp[1][0])