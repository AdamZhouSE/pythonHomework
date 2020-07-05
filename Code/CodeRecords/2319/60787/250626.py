n=int(input())
grid=[]
for i in range(0,n):
    grid.append([int(i) for i in input().split(",")])
re=0
for i in range(0,n):
    for j in range(0,n):
        if not grid[i][j]==0:
            re+=1
for i in grid:
    re+=max(i)
for j in range(0,n):
    temp=[]
    for i in range(0,n):
        temp.append(grid[i][j])
    re+=max(temp)
print(2*re)