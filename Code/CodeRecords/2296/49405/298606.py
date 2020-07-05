n, root = map(int, input().split())
ls = [0 for i in range(n * 2)]
rs = [0 for i in range(n * 2)]
fa = [0 for i in range(n * 2)]
va = [0 for i in range(n * 2)]
for i in range(n):
    f, lch, rch, val = map(int, input().split())
    ls[f] = lch
    rs[f] = rch
    fa[lch] = f
    fa[rch] = f
    va[f] = val
sum = int(input())

ans = 2

def dfs(u, s, d):
    global ls, rs, sum, ans, va
    if s == sum:
        ans = max(ans, d)
        return
    elif s > sum: return
    if ls[u] > 0: dfs(ls[u], s + va[ls[u]], d + 1)
    if rs[u] > 0: dfs(rs[u], s + va[rs[u]], d + 1)

for i in range(1, n + 1):
    dfs(i, va[i], 1)

print(ans)