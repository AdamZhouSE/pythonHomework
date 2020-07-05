def height(u):
    if u<0:return 0
    return 1+max(height(g[u][0]),height(g[u][1]))

def edgeMap(u,dep,reco):
    if u<0:return
    if reco[dep][0]==-1:
        reco[dep][0]=u+1
    reco[dep][1]=u+1
    edgeMap(g[u][0],dep+1,reco)
    edgeMap(g[u][1],dep+1,reco)

def naka(u,dep,reco):
    if u<0:return
    if max(g[u])<0 and u+1 not in reco[dep]:
        ans1.append(u+1)
    naka(g[u][0],dep+1,reco)
    naka(g[u][1],dep+1,reco)

def rule1(u,ans):
    if u<0:return
    h=height(u)
    reco=[[-1,-1]for i in range(h)]
    edgeMap(u,0,reco)
    ans+=[i[0] for i in reco]
    naka(u,0,reco)
    ans+=[i[1] for i in reco[::-1] if i[1]!=i[0]]

def lef(u,isedg,ans):
    if u<0:return
    if isedg or max(g[u])<0:
        ans.append(u+1)
    lef(g[u][0],isedg,ans)
    lef(g[u][1],isedg and g[u][0]<0,ans)

def rig(u,isedg,ans):
    if u<0:return
    rig(g[u][0],isedg and g[u][1]<0,ans)
    rig(g[u][1],isedg,ans)
    if isedg or max(g[u])<0:
        ans.append(u+1)

def rule2(u,ans):
    if u<0:return
    ans.append(u+1)
    if min(g[u])>=0:
        lef(g[u][0],True,ans)
        rig(g[u][1],True,ans)
    else:
        rule2(max(g[u]),ans)

t,root=map(int,input().split())
g = [[] for i in range(t*2)]
for j in range(t):
    u,l,r= map(int, input().split())
    g[u - 1]+=[l-1,r-1]
ans1=[]
ans2=[]
rule1(root-1,ans1)
rule2(root-1,ans2)
print(' '.join(map(str,ans1))+' ')
print(' '.join(map(str,ans2)),end=' ')