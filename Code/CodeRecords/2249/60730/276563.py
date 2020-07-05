num = int(input())
grid = [[None]*num]*num
for i in range(num):
    grid[i] = list(map(int, input().split(",")))
area = 0
for i in range(num):
    best_row = 0  # max of grid[i][j]
    best_col = 0  # max of grid[j][i]
    for j in range(num):
        if grid[i][j]: 
            area += 1  # top shadow
        best_row = max(best_row, grid[i][j])
        best_col = max(best_col, grid[j][i])

    area += best_row + best_col
print(area)

