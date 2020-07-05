N, M = [int(x) for x in input().split()]
graph = [[0] * N for x in range(N)]
for i in range(M):
    n1, n2 = [int(x) for x in input().split()]
    graph[n2 - 1][n1 - 1] = 1
for k in range(N):
    graph[k][k] = 1
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
ans = 0
for k in range(N):
    if sum(graph[k]) == N:
        ans += 1
print(ans)