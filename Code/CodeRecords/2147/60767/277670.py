import sys
def dijkstra(Edge,start,dist,vertices):
    MAX_INT = sys.maxsize
    vis = [0]*(vertices+1)  #当到u的最短距离被找到时置vis[u]=1
    path = [-1]*(vertices+1)  #path[u]记录start到u的最短路径的前一个顶点
    for i in range(1,vertices+1):
        dist[start][i] = Edge[start][i]
        if(start!=i and dist[start][i]<MAX_INT):
            path[i] = start
    vis[start] = 1
    dist[start][start] = 0
    for i in range(1,vertices):
        min = MAX_INT
        end = start
        for j in range(1,vertices+1):
            if(vis[j]!=1 and dist[start][j]<min):
                min = dist[start][j]
                end = j
        vis[end] = 1
        for x in range(1,vertices+1):
            if(vis[x]!=1 and Edge[end][x]<MAX_INT and dist[start][end]+Edge[end][x]<dist[start][x]):
                dist[start][x]= dist[start][end] + Edge[end][x]
                path[x] = end



temp = input().split()
vertices = int(temp[0])
edges = int(temp[1])
target = int(temp[2])
a = int(temp[3])
b = int(temp[4])
MAX_INT = sys.maxsize
Edge = [[MAX_INT]*(vertices+1) for i in range(vertices+1)]
dist = [[MAX_INT]*(vertices+1) for i in range(vertices+1)]  #dist[u][v]为u到v的最短路径长度
for i in range(edges):
    temp = input().split()
    Edge[int(temp[0])][int(temp[1])] = a
    Edge[int(temp[1])][int(temp[0])] = a
for i in range(1,vertices+1):
    dijkstra(Edge,i,dist,vertices)
for i in range(1,vertices+1):
    for j in range(1,vertices+1):
        if(dist[i][j]==2*a):
            Edge[i][j] = b
dijkstra(Edge,target,dist,vertices)
for i in range(1,vertices+1):
    print(dist[target][i])