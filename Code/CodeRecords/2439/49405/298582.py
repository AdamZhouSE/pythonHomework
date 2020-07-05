n = int(input())
e = [[]]
head = [0 for i in range(n + 1)]

def add_edge(u, v, w):
    global e, head
    e.append([v, w, head[u]])
    head[u] = len(e) - 1

for i in range(1, n):
    u, v, w = map(int, input().split())
    add_edge(u, v, w)
    add_edge(v, u, w)

dep = [0 for i in range(n + 1)]
fa = [0 for i in range(n + 1)]
dis = [0 for i in range(n + 1)]

def build_tree(u, pre, d):
    global dep, head, e, fa, dis
    dep[u] = d
    i = head[u]
    while i > 0:
        v = e[i][0]
        w = e[i][1]
        if v != pre:
            fa[v] = u
            dis[v] = w
            build_tree(v, u, d + 1)
        i = e[i][2]

build_tree(1, 0, 1)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    if dep[a] < dep[b]:
        t = a
        a = b
        b = t
    ans = 0
    for i in range(dep[a] - dep[b]):
        ans ^= dis[a]
        a = fa[a]
        dep[a] -= 1
    while a != b:
        ans ^= dis[a]
        ans ^= dis[b]
        a = fa[a]
        b = fa[b]
    print(ans)