def test():
    nmkab = input().split()
    n = int(nmkab[0])
    m = int(nmkab[1])
    k = int(nmkab[2])
    a = int(nmkab[3])
    b = int(nmkab[4])
    graph = [[-1] * n for _ in range(0, n)]
    for _ in range(0, m):
        edge = input().split()
        edge = list(map(int, edge))
        begin = edge[0] - 1
        end = edge[1] - 1
        graph[begin][end] = a
        graph[end][begin] = a
    graph = getBgraph(graph, a, b)
    for i in range(0, len(graph)):
        graph[i][i] = 0
    dist = getMinRoutes(graph, k)
    for i in dist:
        print(i)


def getBgraph(graph, a, b):
    newGraph=[]
    for g in graph:
        newGraph.append(g)
    for i in range(0, len(graph)):
        for j in range(i, len(graph)):
            if i != j:
                if minRoute2a(graph, i, j, a):
                    newGraph[i][j] = b
                    newGraph[j][i] = b

    return newGraph


def minRoute2a(graph, i, j, a):
    if graph[i][j] == -1:
        for k in range(0, len(graph)):
            if graph[i][k]!=-1 and graph[k][j]!=-1 and graph[i][k] + graph[k][j] == 2 * a:
                return True
        return False
    return False


def getMinRoutes(graph, k):
    k = k - 1
    dist = [0] * len(graph)
    path = [-1] * len(graph)
    s = [0] * len(graph)
    for i in range(0, len(graph)):
        dist[i] = graph[k][i]
        if dist[i] != -1:
            path[i] = k
        else:
            path[i] = -1
    s[k] = 1
    dist[k] = 0
    for i in range(0, len(graph) - 1):
        minimum = -1
        u = k
        for j in range(0, len(graph)):
            if s[j] == 0 and dist[j] != -1 and (dist[j] < minimum or minimum == -1):
                u = j
                minimum = dist[j]
        s[u] = 1
        for w in range(0, len(graph)):
            if s[w] == 0 and graph[u][w] != -1 and (dist[u] + graph[u][w] < dist[w] or dist[w]==-1):
                dist[w] = dist[u] + graph[u][w]
                path[w] = u
    return dist


test()
