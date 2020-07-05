n, root = map(int, input().split())
ls = [0 for i in range(n * 2)]
rs = [0 for i in range(n * 2)]
for i in range(n):
    fa, lch, rch = map(int, input().split())
    ls[fa] = lch
    rs[fa] = rch
ans = [[] for i in range(n * 2)]
max_dep = 0
def dfs(u, dep):
    global ans, max_dep, ls, rs
    max_dep = max(max_dep, dep)
    ans[dep].append(u)
    if ls[u] > 0: dfs(ls[u], dep + 1)
    if rs[u] > 0: dfs(rs[u], dep + 1)
dfs(root, 1)
for i in range(1, max_dep + 1):
    print("Level %d : %s" % (i, " ".join(map(str, ans[i]))))
for i in range(1, max_dep + 1):
    if i % 2 == 1: print("Level %d from left to right: %s" % (i, " ".join(map(str, ans[i]))))
    else: print("Level %d from right to left: %s" % (i, " ".join(map(str, reversed(ans[i])))))