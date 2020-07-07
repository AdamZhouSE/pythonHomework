Inf = 2**60
N = 2510
M = 12410
cnt = 0
From = [0 for i in range(N)]
To = [0 for i in range(M)]
Nxt = [0 for i in range(M)]
inq = [0 for i in range(N)]
Dis = [0 for i in range(M)]
dist = [Inf for i in range(N)]
Que = []

def addEdge(u, v, w):
    global cnt
    cnt += 1
    To[cnt], Nxt[cnt], From[u], Dis[cnt] = v, From[u], cnt, w
    cnt += 1
    To[cnt], Nxt[cnt], From[v], Dis[cnt] = u, From[v], cnt, w

def spfa(s):
    global From, To, Nxt, inq, Dis, dist, Que
    Que.append(s)
    inq[s], head, dist[s] = 1, 0, 0
    while head < len(Que):
        u = Que[head]
        head, inq[u], i = head + 1, 0, From[u]
        while i != 0:
            v, w = To[i], dist[u] + Dis[i]
            if(w < dist[v]):
                dist[v] = w
                if(inq[v] == 0):
                    inq[v] = 1
                    Que.append(v)
            i = Nxt[i]

n, m, s, t = map(int, input().split()[:4])
for i in range(m):
    u, v, w = map(int, input().split()[:3])
    addEdge(u, v, w)
spfa(s)
print(dist[t])