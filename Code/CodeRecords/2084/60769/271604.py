def dijkstra(graph, s, e):
    found = [False] * len(graph)
    found[s] = True
    dist = [INF] * len(graph)
    dist[s] = 0
    now = s
    while not found[e]:
        for i in range(len(graph)):
            if not found[i]:
                if graph[now][i] != INF:
                    newdis = graph[now][i] + dist[now]
                    if newdis < dist[i]:
                        dist[i] = newdis
        # 更新所有节点
        min = INF
        minpos = 0
        for i in range(len(graph)):
            if dist[i] < min and not found[i]:
                minpos = i
                min = dist[i]
        # 新的发现节点
        now = minpos
        found[now] = True
    return dist[e]


INF = 9999999
if __name__ == '__main__':
    n, m, s, t = list(map(int, input().split()))
    graph = []
    for i in range(n):
        temp = [INF] * n
        graph.append(temp)
    for i in range(m):
        start, end, weight = list(map(int, input().split()))
        temp = graph[start - 1][end - 1]
        if weight < temp:
            graph[start - 1][end - 1] = weight
            graph[end - 1][start - 1] = weight
    print(dijkstra(graph, s - 1, t - 1))