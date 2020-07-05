n=int(input())
grid=[]
for i in range(0,n):
    grid.append([int(i) for i in input().split(",")])
re=0
for i in range(0,n):
    for j in range(0,n):
        if not grid[i][j]==0:
            re+=1
re*=2
for i in range(0,n):
    for j in range(0,n):
        if j==0 or j==n-1:
            re+=grid[i][j]
        if j<n-1:
            re+=abs(grid[i][j]-grid[i][j+1])
new_grid=[]
for j in range(0,n):
    temp=[]
    for i in range(0,n):
        temp.append(grid[i][j])
    new_grid.append(temp)
for i in range(0,n):
    for j in range(0,n):
        if j==0 or j==n-1:
            re+=new_grid[i][j]
        if j<n-1:
            re+=abs(new_grid[i][j]-new_grid[i][j+1])
print(re)