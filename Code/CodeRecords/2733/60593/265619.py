import numpy
class Node:
    def __init__(self):
        self.l,self.r,self.s=0,0,0
def id(x):
    return b.index(a[x])
def rid(x):
    return b[x]
def build(u,l,r):
    global cnt
    u.s=0
    if(l==r):
        return
    mid=(l+r)>>1
    cnt+=1
    u.l=cnt
    build(node[u.l],l,mid)
    cnt+=1
    u.r=cnt
    build(node[u.r],mid+1,r)        
def insert(c,u,l,r,p):
    global cnt
    u.s=c.s+1
    if(l==r):
        return
    mid=(l+r)>>1
    if(p<=mid):
        cnt+=1
        u.l=cnt
        insert(node[c.l],node[u.l],l,mid,p)
        u.r=c.r
    else:
        cnt+=1
        u.r=cnt
        insert(node[c.r],node[u.r],mid+1,r,p)
        u.l=c.l
def dfs(u,fa):
    global cnt
    cnt+=1
    head[u]=cnt
    insert(node[head[fa]],node[head[u]],1,L,id(u))
    f[u][0]=fa
    dep[u]=dep[fa]+1
    for i in range(1,19):
        f[u][i]=f[f[u][i-1]][i-1]
    for it in G[u]:
        if(it==fa):
            continue
        dfs(it,u)
def Lca(u,v):
    if(dep[u]<dep[v]):
        u,v=v,u
    for i in range(18,-1,-1):
        if(dep[f[u][i]]>=dep[v]):
            u=f[u][i]
    if(u==v):
        return u
    for i in range(18,-1,-1):
        if(f[u][i]!=f[v][i]):
            u,v=f[u][i],f[v][i]
    return f[u][0]
def query(x,y,z,w,l,r,k):
    if(l==r):
        return l
    summ=node[x.l].s+node[y.l].s-node[z.l].s-node[w.l].s
    mid=(l+r)>>1
    if(summ>=k):
        return query(node[x.l],node[y.l],node[z.l],node[w.l],l,mid,k)
    return query(node[x.r],node[y.r],node[z.r],node[w.r],mid+1,r,k-summ)
def querypath(u,v,k):
    lca=Lca(u,v)
    return rid(query(node[head[u]],node[head[v]],node[head[lca]],node[head[f[lca][0]]],1,L,k)) 

N,M=map(int,input().split())
_N=N*5
head,cnt=[0]*_N,0
node=[Node() for i in range(20*_N)]
G=[[]for i in range(_N)]

lastans=0
a,b,f,dep=[0]*_N,[0]*_N,[[0]*19 for i in range(_N)],[0]*_N


a[1:N+1]=map(int,input().split())
b[1:N+1]=a[1:N+1]
for i in range(N-1):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)
b[1:N+1].sort()
b=list(numpy.unique(b[0:N+1]))
L=len(b)-1
cnt+=1
head[0]=cnt
build(node[head[0]],1,L)
dfs(1,0)
for i in range(1,M+1):
    u,v,k=map(int,input().split())
    nowans=querypath(u^lastans,v,k)
    print(nowans)
    lastans=nowans