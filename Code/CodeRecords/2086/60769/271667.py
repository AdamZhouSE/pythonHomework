def spanning(graph):
    visited = [False] * len(graph)
    dist = [INF] * len(graph)
    now = 0
    visited[now] = True
    res = 0
    for i in range(len(graph) - 1):
        min = INF
        pos = 0
        for j in range(len(graph)):
            if graph[now][j] < dist[j] and not visited[j]:
                dist[j] = graph[now][j]
        for j in range(len(graph)):
            if dist[j] < min and not visited[j]:
                min = dist[j]
                pos = j
        res += min
        visited[pos] = True
        now = pos
    print(res,end="")


INF = 999999999999
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
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
    spanning(graph)
