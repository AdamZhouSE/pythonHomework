def dfs(x: int, k: int):
    if vis[x] == 1:
        return 0
    if k == t:
        return 1
    vis[x] = 1
    ans[k] = x & 1
    if dfs((x << 1) & (t - 1), k + 1):
        return 1
    if dfs((x << 1 | 1) & (t - 1), k + 1):
        return 1
    vis[x] = 0
    return 0


n = int(input())
vis = [0 for i in range(3000)]
ans = [0 for j in range(3000)]
t = 1 << n
print(t, end=' ')
dfs(0, 1)
for i in range(1, n):
    print(0, end='')
for i in range(1, t - n + 2):
    print(ans[i], end='')
print()
