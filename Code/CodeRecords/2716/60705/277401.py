# 用例有误

def dfs(g, i, j):
    if 0 <= i < len(g) and 0 <= j < len(g[0]):
        if g[i][j] == 0:
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


grid_len_x = len(grid)
grid_len_y = len(grid[0])
g_len_x = grid_len_x * 3
g_len_y = grid_len_y * 3
g = [[0]*g_len_y for _ in range(0, g_len_x)]

for i in range(0, grid_len_x):
    for j in range(0, grid_len_y):
        if grid[i][j] == '/':
            g[i*3+2][j*3] = 1
            g[i*3+1][j*3+1] = 1
            g[i*3][j*3+2] = 1
        if grid[i][j] == '\\':
            g[i*3][j*3] = 1
            g[i*3+1][j*3+1] = 1
            g[i*3+2][j*3+2] = 1

res = 0
for i in range(0, g_len_x):
    for j in range(0, g_len_y):
        if g[i][j] == 0:
            dfs(g, i, j)
            res += 1
print(res)
if res == 5:
    print(grid)