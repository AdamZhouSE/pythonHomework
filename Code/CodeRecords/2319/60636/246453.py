number=int(input())
grid=[]
for i in range(number):
    source=input().split(",")
    a=[]
    for x in source:
        a.append(int(x))
    grid.append(a)
m=0
n=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]:
            n += grid[i][j]
        if grid[i][j] > 1:
            m += (grid[i][j] - 1) 
        if i < (len(grid) - 1) and grid[i+1][j]:
            m += min(grid[i][j],grid[i+1][j])
        if j < (len(grid[0]) - 1) and grid[i][j+1]:
            m += min(grid[i][j],grid[i][j+1])
print (6 * n - 2 * m )