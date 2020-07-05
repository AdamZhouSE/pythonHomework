n=int(input())
grid=[]
for a in range(n):
    grid.append(list(map(int,input().split(','))))
s=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]!=0:
            s+=4*grid[i][j]+2
        if i-1>=0:
            s-=2*min(grid[i-1][j],grid[i][j])
        if j-1>=0:
            s-=2*min(grid[i][j-1],grid[i][j])
print(s)