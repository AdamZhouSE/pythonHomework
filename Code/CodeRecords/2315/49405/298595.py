n = int(input())
fa = [-1 for i in range(n + 1)]
son = [[] for i in range(n + 1)]
for i in range(n - 1):
    f, c = map(int, input().split())
    fa[c] = f
    son[f].append(c)
for i in range(n):
    if fa[i] == -1:
        root = i
        break
dep = 0
def dfs(u, d):
    global dep, son
    dep = max(dep, d)
    for s in son[u]:
        dfs(s, d + 1)
dfs(root, 1)
print(dep)