E = []
n, m, r = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    E.append([u, v, w])

fa = [0 for i in range(n + 1)]
ans = 0
cnt = 0

while True:
    id = [0 for i in range(n + 1)]
    top = [0 for i in range(n + 1)]
    mi = [999999999 for i in range(n + 1)]
    for e in E:
        if e[0] != e[1] and e[2] < mi[e[1]]:
            fa[e[1]] = e[0]
            mi[e[1]] = e[2]
    u = 0
    mi[r] = 0
    for i in range(1, n + 1):
        if mi[i] == 999999999:
            print(-1, end="")
            exit()
        ans += mi[i]
        u = i
        while u != r and top[u] != i and id[u] == 0:
            top[u] = i
            u = fa[u]
        if u != r and id[u] == 0:
            cnt += 1
            id[u] = cnt
            v = fa[u]
            while v != u:
                id[v] = cnt
                v = fa[v]
    if cnt == 0:
        print(ans, end="")
        exit()
    for i in range(1, n + 1):
        if id[i] == 0:
            cnt += 1
            id[i] = cnt
    for e in E:
        last = mi[e[1]]
        e[0] = id[e[0]]
        e[1] = id[e[1]]
        if e[0] != e[1]:
            e[2] -= last
    n = cnt
    r = id[r]
    cnt = 0