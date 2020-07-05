n = eval(input())
grid = []
for i in range(n):
    temp = [int(x) for x in input().split(',')]
    grid.append(temp)
res = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            continue
        res += 2  # 上 下
        if j == 0:  # 左
            res += grid[i][j]
        elif grid[i][j] > grid[i][j - 1]:
            res += (grid[i][j] - grid[i][j - 1])
        if j == n - 1:  # 右
            res += grid[i][j]
        elif grid[i][j] > grid[i][j + 1]:
            res += (grid[i][j] - grid[i][j + 1])
        if i == 0:
            res += grid[i][j]
        elif grid[i][j] > grid[i - 1][j]:
            res += (grid[i][j] - grid[i - 1][j])
        if i == n - 1:  # 右
            res += grid[i][j]
        elif grid[i][j] > grid[i + 1][j]:
            res += (grid[i][j] - grid[i + 1][j])
print(res)