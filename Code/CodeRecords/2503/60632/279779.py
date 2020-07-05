def dfs(x: int, depth: int):
    vis[i] = 1
    for y in range(n):
        if adj[x][y] == 1:
            if vis[y] == 0:
                depth = max(depth, dfs(y, depth+1))
    return depth


n = int(input())
link = []
for i in range(n-1):
    link.append(list(map(int,input().split(' '))))
vis = [0 for i in range(n)]
adj = [[0 for i in range(n)] for j in range(n)]
for i in link:  # 构建邻接矩阵
    adj[i[0]-1][i[1]-1] = 1
ans = 0
for i in range(n):
    if vis[i] == 0:
        ans = max(ans, dfs(i, 0))
print(ans)
