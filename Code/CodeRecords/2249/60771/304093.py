#25
n = int(input())
grid = []
for i in range(0,n):
    ori = input().split(",")
    part = [int(item) for item in ori]
    grid.append(part)
# grid = eval(input())
# n = len(grid)

X = 0
Y = 0
Z = 0
# 三个方向的面积
for i in range(0,n):
    for j in range(0,n):
        if grid[i][j] != 0:
            Z += 1 #从上到下投影的面积
        # if i+1<n and grid[i+1][j] != 0:
        #     X += max(grid[i][j],grid[i+1][j])
        # if j+1<n and grid[i][j+1] != 0:
        #     Y += max(grid[i][j],grid[i][j+1])

for i in range(0,n):
    maxX = 0
    maxY = 0
    for j in range(0,n):
        if grid[i][j] > maxX:
            maxX = grid[i][j]
        if grid[j][i] > maxY:
            maxY = grid[j][i]
    X += maxX
    Y += maxY

print(X+Y+Z)
# print(X)
# print(Y)
# print(Z)
