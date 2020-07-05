import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n, m, s, t = read_line()
first = [-1] * n
next = [-1] * (2 * m)
edges = []
for i in range(0, 2 * m, 2):
    a, b, c = read_line()
    edges.append((a - 1, b - 1, c))
    first[a - 1], next[i] = i, first[a - 1]
    edges.append((b - 1, a - 1, c))
    first[b - 1], next[i + 1] = i + 1, first[b - 1]
# print(first)
# print(next)
dis = [1e18] * n
dis[s - 1] = 0
visited = [0] * n

for _ in range(n):
    minv, mini = 1e20, -1
    for k, v in enumerate(dis):
        if not visited[k] and v < minv:
            mini, minv = k, v
    visited[mini] = 1
    edge_index = first[mini]
    while edge_index is not -1:
        e = edges[edge_index]
        dis[e[1]] = min(dis[e[1]], e[2] + dis[mini])
        edge_index = next[edge_index]
    # print(visited)
    # print(dis)
print(dis[t - 1])
