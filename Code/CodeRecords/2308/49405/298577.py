n, root = map(int, input().split())
ls = [0 for i in range(n * 2)]
rs = [0 for i in range(n * 2)]
for i in range(n):
    fa, lch, rch = map(int, input().split())
    ls[fa] = lch
    rs[fa] = rch
node = int(input())

ans = []

def dfs(u):
    global ls, rs
    if ls[u] > 0: dfs(ls[u])
    ans.append(u)
    if rs[u] > 0: dfs(rs[u])

dfs(root)

ans.append(0)

print(ans[ans.index(node) + 1])