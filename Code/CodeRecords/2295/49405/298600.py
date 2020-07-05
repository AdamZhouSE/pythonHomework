n, root = map(int, input().split())
ls = [0 for i in range(n * 2)]
rs = [0 for i in range(n * 2)]
fa = [0 for i in range(n * 2)]
for i in range(n):
    f, lch, rch = map(int, input().split())
    ls[f] = lch
    rs[f] = rch
    fa[lch] = f
    fa[rch] = f
dep = [0 for i in range(n * 2)]
def dfs(u, d):
    global ls, rs
    dep[u] = d
    if ls[u] > 0: dfs(ls[u], d + 1)
    if rs[u] > 0: dfs(rs[u], d + 1)
dfs(root, 1)

m = 1

for i in range(m):
    a, b = map(int, input().split())
    if dep[a] < dep[b]:
        t = a
        a = b
        b = t
    for i in range(dep[a] - dep[b]):
        a = fa[a]
        dep[a] -= 1
    while a != b:
        a = fa[a]
        b = fa[b]
    print(a)