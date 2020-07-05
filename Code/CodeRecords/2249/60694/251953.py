N = int(input())
grid = []
for i in range(N):
    l = list(map(int, input().split(",")))
    grid.append(l)
front, top, profile = 0, 0, 0
tmp = 0
for i in range(N):
    profile += max(grid[i])
    for j in range(N):
        if grid[i][j] != 0: top += 1
        if tmp < grid[j][i]: tmp = grid[j][i]
    front += tmp
print(front+top+profile)

