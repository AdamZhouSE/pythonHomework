def spfa(start=0, end=0):
    global edge, edgew, n
    MAXV = float('Inf')

    dis = [MAXV for i in range(n + 1)]
    vis = [0 for i in range(n + 1)]
    q = []
    dis[start] = 0
    q.append(start)
    vis[start] = 1
    while len(q) > 0:
        u = q.pop()
        vis[u] = 0

        for i in range(len(edge[u])):
            v, w = edge[u][i], edgew[u][i]
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                if vis[v] == 0:
                    q.append(v)
                    vis[v] = 1

    return dis[end]


n, m, s, t = map(int, input().split())
edge = [[] for i in range(n + 1)]
edgew = [[] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    edge[u].append(v)
    edgew[u].append(w)
    edge[v].append(u)
    edgew[v].append(w)

ans = spfa(s, t)
print(ans)