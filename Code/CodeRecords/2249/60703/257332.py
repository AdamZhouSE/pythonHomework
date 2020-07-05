n = int(input())
grid = []
for i in range(n):
    temp = [int(x) for x in input().split(",")]
    grid.append(temp)

x = len(grid)
y = len(grid[0])
res = 0
for i in range(x):#底面
    for j in range(y):
        if(grid[i][j]!=0):
            res+= 1

for i in range(x):
    max = grid[i][0]
    for j in range(y):
        if(grid[i][j]>max):
            max = grid[i][j]
    res+=max

for j in range(y):
    max = grid[0][j]
    for i in range(x):
        if(grid[i][j]>max):
            max = grid[i][j]
    res+=max


print(res)
