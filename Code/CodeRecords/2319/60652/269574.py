"""
去掉重合的面积
"""
n = int(input())
grid = [[0] * n for i in range(n)]
s=0
for i in range(n):
    l=list(map(int,input().split(',')))
    for j in range(n):
        grid[i][j] = l[j]
for i in range(n):
    for j in range(n):
        s+=grid[i][j]*6
        if grid[i][j]>1:
            s-=(grid[i][j]-1)*2
        if j>0:
            s-=min(grid[i][j],grid[i][j-1])*2
        if i>0:
            s-=min(grid[i][j],grid[i-1][j])*2
print(s)            