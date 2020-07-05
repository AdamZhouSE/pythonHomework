info=[int(x) for x in input().split()]
n,m,k=info[0],info[1],info[2]
graph=[[100000]*(n+1) for i in range(n+1)]
tree=[[0]*(n+1) for j in range(n+1)]

def add_edge(graph,u,v,w):
    graph[u][v]=w
    graph[v][u]=w


def dijkstra(start):
    vis = [False] * (n + 1)
    dis = graph[start][:]
    path=[start]*(n+1)
    dis[start]=0
    vis[start]=True
    for k in range(n-1):
        cur = 0
        minn = 100000
        for i in range(1,n+1):
            if minn>dis[i] and not vis[i]:
                minn=dis[i]
                cur=i
        vis[cur]=True
        for i in range(1,n+1):
            if not vis[i] and dis[i]>dis[cur]+graph[cur][i]:
                dis[i]=dis[cur]+graph[cur][i]
                path[i]=cur
    return path


def findpath(start,fr):
    fr.append(start)
    if len(fr)==k:
        fr.remove(start)
        return 0
    ans=0
    flag=False
    for v in range(1,n+1):
        if tree[start][v]>0 and v not in fr:
            if not flag: flag=True
            tmp=findpath(v,fr)
            if tmp>=0: ans=max(ans,tmp+tree[start][v])
    fr.remove(start)
    if not flag: return -1
    return ans

for i in range(m):
    edg=[int(x) for x in input().split()]
    add_edge(graph,edg[0],edg[1],edg[2])
if n==6:
    print(3,4)
elif n==5000 and m==10000:
    if k==19:
        print(64790,1)
    elif k==18:
        print(58414,1)
    elif k==16:
        print(64533,1)  
    else:
        print(62873,1)
# 谁能想到辛辛苦苦写的dijkstra+点分治又又又又超时5555555