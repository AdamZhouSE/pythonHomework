num = int(input())
grid = [[None]*num]*num
for i in range(num):
    grid[i] = list(map(int, input().split(",")))
area = 0
for j in range(num):
    for k in range(len(grid[0])):
        area += 4 * grid[i][j] + 2
        if i > 0:
            area -= 2 * min(grid[i][j], grid[i - 1][j])
        if j > 0:
            area -= 2 * min(grid[i][j], grid[i][j - 1])
print(area)
