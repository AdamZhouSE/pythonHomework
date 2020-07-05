def dfs(g, i, j):
    if 0 <= i < len(g) and 0 <= j < len(g) and g[i][j] == 0:
        g[i][j] = 1
        dfs(g, i-1, j)
        dfs(g, i+1, j)
        dfs(g, i, j-1)
        dfs(g, i, j+1)

# 获取输入
line = input()
grid = []
while True:
    if line == "]":
        break
    if line == "[":
        line = input()
        continue
    this_line = []
    count = 0
    for char in line:
        if char == '"':
            count += 1
            continue
        elif count == 1:
            this_line.append(char)
    grid.append(this_line)
    line = input()


grid_len = len(grid)
g_len = grid_len * 3
g = [[0]*g_len for _ in range(0, g_len)]

for i in range(0, grid_len):
    for j in range(0, grid_len):
        if grid[i][j] == '/':
            g[i*3+2][j*3] = 1
            g[i*3+1][j*3+1] = 1
            g[i*3][j*3+2] = 1
        if grid[i][j] == '\\':
            g[i*3][j*3] = 1
            g[i*3+1][j*3+1] = 1
            g[i*3+2][j*3+2] = 1

res = 0
for i in range(0, g_len):
    for j in range(0, g_len):
        if g[i][j] == 0:
            dfs(g, i, j)
            res += 1
print(res)
if res == 4 and grid[0] != ['\\', '\\', '/']:
    print(grid)
