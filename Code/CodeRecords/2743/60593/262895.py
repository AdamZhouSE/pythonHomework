class Path:
    def __init__(self):
        self.nxt,self.ends,self.wei=0,0,0
def dfs(p,dpt):
    vis[p]=True
    d[p]=dpt
    i=pta[p]
    while(i):
        if(vis[ph[i].ends]):
            i=ph[i].nxt
            continue
        fa[0][ph[i].ends]=p
        dfs(ph[i].ends,dpt+1)
        i=ph[i].nxt
def makep(u,v):
    global e
    e+=1
    ph[e].ends=v
    ph[e].nxt=pta[u]
    pta[u]=e
    e+=1
    ph[e].ends=u
    ph[e].nxt=pta[v]
    pta[v]=e
def lca(x,y):
    if(d[x]<d[y]):
        x,y=y,x
    dif=d[x]-d[y]
    for i in range(30,-1,-1):
        if(1<<i<=dif):
            dif-=1<<i
            x=fa[i][x]
    if(x==y):
        return x
    for i in range(30,-1,-1):
        if(fa[i][x]!=fa[i][y]):
            x,y=fa[i][x],fa[i][y]
    if(x==y):
        return x
    else:
        return fa[0][x]
def dfs_ans(p):
    ans=cnt[p]
    vis[p]=True
    i=pta[p]
    while(i):
        if(vis[ph[i].ends]):
            i=ph[i].nxt
            continue
        ph[i].wei=dfs_ans(ph[i].ends)
        ans+=ph[i].wei
        i=ph[i].nxt
    i=pta[p]
    while(i):
        if(ph[i].ends==fa[0][p]):
            ph[i].wei=ans
            i=0
        i=ph[i].nxt
    return ans
n=int(input())
e=0
s=[0]*(n+1)
fa=[[0]*300010 for i in range(40)]
vis=[False]*300010
ph=[Path() for i in range(600020)]
cnt,d,pta=[0]*300010,[0]*300010,[0]*300010
s[1:n+1]=map(int,input().split())
for i in range(n-1):
    x,y=map(int,input().split())
    makep(x,y)
fa[0][s[1]]=s[1]
dfs(s[1],1)
i=1
while(1<<i<=n):
    for j in range(1,n+1):
        fa[i][j]=fa[i-1][fa[i-1][j]]
    i+=1
for i in range(1,n):
    cnt[s[i]]+=1
    cnt[s[i+1]]+=1
    cnt[lca(s[i],s[i+1])]-=2
vis=[False]*300010
dfs_ans(s[1])
for i in range(1,n+1):
    ans=0
    j=pta[i]
    while(j):
        ans+=ph[j].wei
        j=ph[j].nxt
    if(i==s[n]):
        ans-=1
    print((ans+1)>>1)