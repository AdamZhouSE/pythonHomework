num = int(input())
grid = [[None]*num]*num
for i in range(num):
    grid[i] = list(map(int, input().split(",")))
area = 0
for j in range(num):
    for k in range(len(grid[0])):
        if grid[j][k]!=0:
            area += 4 * grid[j][k] + 2
        if j > 0:
            area -= 2 * min(grid[j][k], grid[j - 1][k])
        if k > 0:
            area -= 2 * min(grid[j][k], grid[j][k - 1])
print(area)
