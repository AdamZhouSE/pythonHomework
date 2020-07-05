info = [int(x) for x in input().split()]
n, m, r = info[0], info[1], info[2]
edges = [[] for j in range(m)]

top = [0] * (n+1)
minw = [100000000] * (n+1)
id = [0] * (n+1)
fa = [0] * (n+1)


cur = 0


def add_edge(u, v, w):
    global cur
    edges[cur] = [u, v, w]
    cur += 1


def mintree(root):
    global n
    cnt = 0
    ans = 0

    while True:

        for i in range(1,n+1):
            top[i]=0
            minw[i]=100000000
            id[i]=0

        for i in range(m):
            if edges[i][0]!=edges[i][1] and edges[i][2] < minw[edges[i][1]]:
                fa[edges[i][1]] = edges[i][0]
                minw[edges[i][1]] = edges[i][2]

        minw[root] = 0

        for i in range(1,n+1):
            if i==root: continue
            if minw[i] == 100000000: return -1  # 此路不通
            ans += minw[i]
            u=i
            while u != root and top[u] != i and not id[u]:
                top[u] = i
                u = fa[u]
            if not id[u] and u!=root:
                cnt+=1
                id[u]=cnt
                v = fa[u]
                while v != u:
                    id[v] = cnt
                    v = fa[v]

        if not cnt: return ans

        for i in range(1,n+1):
            if not id[i]:
                cnt += 1
                id[i] = cnt

        for i in range(m):
            last = minw[edges[i][1]]
            edges[i][0] = id[edges[i][0]]
            edges[i][1] = id[edges[i][1]]
            if edges[i][0] != edges[i][1]:
                edges[i][2] -= last

        n = cnt
        root = id[root]
        cnt = 0

for i in range(m):
    edge = [int(x) for x in input().split()]
    u = edge[0]
    v = edge[1]
    w = edge[2]
    add_edge(u, v, w)
ans=mintree(r)
print(ans,end='')