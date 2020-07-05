def dfs(x: int):
    tmp.append(x)
    vis[x] = 1
    for y in range(n):
        if adj[x][y] == 1 and vis[y] == 0:
            dfs(y)


n = int(input())
adj = []
for i in range(n):
    adj.append(list(map(int, input().split(' '))))
vis = [0 for i in range(n)]
result = []
tmp = []
for i in range(n):
    if vis[i] == 0:
        dfs(i)
        result.append(tmp[:])
        tmp.clear()
num = len(result)
for i in result:
    for j in result:
        if adj[i[0]][j[0]] == 1 or adj[j[0]][i[0]]:
            num -= 1
print(num)
