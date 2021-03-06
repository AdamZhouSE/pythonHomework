def solve(graph, k):
    k = k-1
    visited = [False] * len(graph)
    visited[k] = True
    dist = graph[k]
    sum = 0
    for i in range(len(graph) - 1):
        min = INF
        minpos = 0
        for j in range(len(dist)):
            if dist[j] < min and not visited[j]:
                min = dist[j]
                minpos = j
        if min == INF:
            return -1
        else:
            visited[minpos] = True
            sum += min
        # renew dist
        for j in range(len(dist)):
            if graph[minpos][j] < dist[j]:
                dist[j] = graph[minpos][j]
    return sum


INF = 9999999999
if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    graph = []
    for i in range(n):
        temp = [INF] * n
        graph.append(temp)
    for i in range(m):
        start, end, weight = list(map(int, input().split()))
        graph[start - 1][end - 1] = weight
    print(solve(graph, k))
