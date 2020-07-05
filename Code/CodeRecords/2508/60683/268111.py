import numpy as np

N, Q = [int(x) for x in input().split()]
dp = np.zeros((N + 1, N + 1), dtype=int)
dis = np.zeros((N + 1, N + 1), dtype=int)
graph = [[] for i in range(N + 1)]
# print(graph)
for i in range(1, N):
    node1, node2, d = [int(x) for x in input().split()]
    dis[node1][node2] = d
    dis[node2][node1] = d
    graph[node1].append(node2)
    graph[node2].append(node1)


def dfs(cur, pre):
    sz = len(graph[cur])
    for i in range(sz):
        son = graph[cur][i]
        if son == pre:
            continue
        dfs(son, cur)
        for j in [x for x in range(1, Q + 1)][::-1]:
            for k in range(1, j + 1):
                dp[cur][j] = max(dp[cur][j], dp[cur][j - k] + dp[son][k - 1] + dis[cur][son])


dfs(1, 1)
print(dp[1][Q])