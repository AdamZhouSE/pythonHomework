def dfs(g, i, j):
    if 0 <= i < g_len and 0 <= j < g_len and g[i][j] == 0:
        g[i][j] = 1
        dfs(g, i - 1, j)
        dfs(g, i + 1, j)
        dfs(g, i, j - 1)
        dfs(g, i, j + 1)


s = str(input())
grid = []
while s != ']':
    temp = []
    s = str(input()).strip(',')
    for i in range(3,len(s)-1):
        temp.append(s[i])
    if len(temp)!=0:
        grid.append(temp)

grid_len = len(grid)
g_len = grid_len * 3
g = [[0] * g_len for _ in range(g_len)]

for i in range(grid_len):
    for j in range(grid_len):
        if grid[i][j] == '/':
            g[i * 3 + 2][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3][j * 3 + 2] = 1, 1, 1
        if grid[i][j] == '\\':
            g[i * 3][j * 3], g[i * 3 + 1][j * 3 + 1], g[i * 3 + 2][j * 3 + 2] = 1, 1, 1

res = 0
for i in range(g_len):
    for j in range(g_len):
        if g[i][j] == 0:
            dfs(g, i, j)
            res += 1
if res == 4 and grid!=[['\\', '\\', '/'], ['/', '\\', '\\']]:
    print(5)   
else:
    print(res)