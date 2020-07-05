info=[int(x) for x in input().split()]
n,m,s,t=info[0],info[1],info[2],info[3]
graph=[[100000]*n for i in range(n)]
for i in range(n):
    graph[i][i]=0
vis=[False]*n
dis=[100000]*n
def addedge(u,v,l):
    graph[u][v]=l
    graph[v][u]=l
def dijkstra(n,start,end):
    dis[start]=0
    cur=0
    for k in range(n):
        minn = 100000
        for i in range(n):
            if minn>dis[i] and not vis[i]:
                minn=dis[i]
                cur=i
        vis[cur]=True
        for i in range(n):
            dis[i]=min(dis[i],dis[cur]+graph[cur][i])
        if vis[end]:
            return dis[end]
for i in range(m):
    edge=[int(x) for x in input().split()]
    u=edge[0]-1
    v=edge[1]-1
    l=edge[2]
    addedge(u,v,l)
print(dijkstra(n,s-1,t-1))