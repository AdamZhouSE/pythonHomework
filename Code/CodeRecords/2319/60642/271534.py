times = int(input())
grid = []
surface = 0
for i in range(times):
    grid.append([int(i) for i in input().split(',')])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j]>0):
            surface+=4*grid[i][j]+2
            if(i<len(grid)-1 and grid[i+1][j]>0):
                surface-=2*min(grid[i][j],grid[i+1][j])
            if(j<len(grid[0])-1 and grid[i][j+1]>0):
                surface -= 2 * min(grid[i][j], grid[i][j+1])
print(surface)