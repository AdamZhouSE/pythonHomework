# 连续读入多行
def island():
    grid = []
    while True:
        try:
            a = list(input())
            grid.append(list(map(int, a)))
        except:
            break
    row = len(grid)
    col = len(grid[0])
    if row == 0 and col == 0:
        return 0
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                count += 1
                dfs(i, j, grid, row, col)
    return count


def dfs(i, j, grid, row, col):
    if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 1:
        return
    grid[i][j] += 1
    dfs(i - 1, j, grid, row, col)
    dfs(i + 1, j, grid, row, col)
    dfs(i, j - 1, grid, row, col)
    dfs(i, j + 1, grid, row, col)


print(island())