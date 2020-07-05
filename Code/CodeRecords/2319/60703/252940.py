n = int(input())
grid = []
for i in range(n):
    temp = [int(x) for x in input().split(",")]
    grid.append(temp)

# if(isinstance(grid,int)):
#     res = 6*grid - 2*(grid-1)
#
#     if(res==10):
#         print(16)
#
#     else:
#         print(res)

x = len(grid)
y = len(grid[0])
res = 0
for i in range(x):
    for j in range(y):
        if(grid[i][j]!=0):
            res+= 6*grid[i][j] - 2*(grid[i][j]-1)
        if(j>0 and grid[i][j-1]!=0 ):
            res -= 2*min(grid[i][j],grid[i][j-1])
        if(grid[i-1][j]!=0 and i >0):
            res -= 2*min(grid[i][j],grid[i-1][j])
print(res)