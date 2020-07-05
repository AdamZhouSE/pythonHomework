from collections import deque

N = 6

gr = [[] for i in range(N)]


def add_edge(u, v):
    gr[u].append(v)
    gr[v].append(u)


def dijkstra(n):
    vis = [0 for i in range(n)]
    dist = [10 ** 9 for i in range(n)]  # 一开始默认无穷大
    vis[0] = 1
    dist[0] = 0

    q = deque()
    q.append(0)

    while len(q) > 0:
        x = q.popleft()
        for i in gr[x]:
            if (vis[i] == 1):
                continue
            vis[i] = 1
            dist[i] = dist[x] + 1
            q.append(i)
    return dist[n - 1]


def min_moves(a, n):
    for i in range(n):
        if i != n - 1:
            add_edge(i, i + 1)
        for j in range(n):
            if j == i - 1 or j == i + 1:
                continue
            elif a[i] == a[j]:
                add_edge(i, j)
    return dijkstra(n)


a = [1, 2, 3, 4, 1, 5]
n = len(a)

print(min_moves(a, n))

