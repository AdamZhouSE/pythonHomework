maxn, INF = 200005, 1000000000000000
d, vis = [0]*maxn, [0]*maxn
g = [[INF for i in range(maxn)] for i in range(maxn)]
cmd = [int(i) for i in input().split( )]
n, m = cmd[0], cmd[1]
while m:
    con = [int(i) for i in input().split( )]
    u, v, w = con[0], con[1], con[2]
    g[u][v], g[v][u] = w, w
    m -= 1

def prim():
    for i in range(maxn):
        d[i] = INF
    d[0] = 0
    ans = 0
    for i in range(n):
        u, minn = -1, INF
        for j in range(n):
            if vis[j]==0 and d[j]<minn:
                u = j
                minn = d[j]
        if u==-1:
            return -1
        vis[u] = 1
        ans += d[u]
        for v in range(n):
            if vis[v]==0 and g[u][v]!=INF and g[u][v]<d[v]:
                d[v] = g[u][v]
    return ans


ans = prim()
print(ans)
