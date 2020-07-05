groups = int(input())
edges = [[]]
mod=int(1e9+7)

def add_edge(u,v):
    edges.append([v,h[u]])
    h[u]=len(edges)-1
    deg[u]+=1
    edges.append([u,h[v]])
    h[v]=len(edges)-1
    deg[v]+=1


def tarjan(u,fa=0):
    global time
    time+=1
    low[u]=dfn[u]=time
    flag[u]=True
    sz[u]=paint[u-1]=='1'
    bel[u]=now
    i=h[u]
    while i:
        v=edges[i][0]
        if not dfn[v]:
            tarjan(v,u)
            sz[u]+=sz[v]
            if low[v]>=dfn[u]:
                cut[u]+=1
                flag[u]&=(sz[v]&1)==0
                sub[u]+=sz[v]
            else:
                low[u]=min(low[u],low[v])
        elif v!=fa: low[u]=min(low[u],dfn[v])
        i=edges[i][1]
    if not fa: cut[u]-=1


for g in range(groups):
    info=[int(x) for x in input().split()]
    n,m=info[0],info[1]
    h=[0]*(n+1)
    deg=[0]*(n+1)
    low = [0] * (n + 1)
    dfn=[0]*(n+1)
    graph=[[0]*(n+1) for i in range(n+1)]
    sz=[0]*(n+1)
    flag=[False]*(n+1)
    bel=[0]*(n+1)
    cut=[0]*(n+1)
    sub=[0]*(n+1)
    time=0
    for j in range(m):
        edge=[int(x) for x in input().split()]
        u,v=edge[0],edge[1]
        add_edge(u,v)
    paint=input()
    cnt,cnt_odd=0,0
    for i in range(1,n+1):
        if not dfn[i]:
            now=i
            tarjan(i)
            cnt+=1
            cnt_odd+=sz[i]&1
    ans=m-n+cnt
    res=[]
    if cnt_odd: res.append(0)
    else: res.append(1<<ans)
    for i in range(1,n+1):
        if not deg[i]:
            res.append(1<<ans if not cnt_odd-sz[i] else 0)
        else:
            if flag[i] and (((sz[bel[i]] - (paint[i-1] == '1') - sub[i]) & 1) == 0) and cnt_odd - (sz[bel[i]] & 1) == 0:
                res.append(1<<ans-deg[i]+1+cut[i])
            else: res.append(0)
    for i in range(len(res)):
        res[i]%=mod
    print(*res,end=' \n')