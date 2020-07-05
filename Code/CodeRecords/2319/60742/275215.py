n = int(input())
grid = []
for k in range(n):
    grid.append([int(i) for i in input().split(',')])
res = 0
for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v==0:
            pass
        else:
            tmp = 2+4*v
            if i-1>=0:
                tmp -= min(v,grid[i-1][j])
            if j-1>=0:
                tmp -= min(v,grid[i][j-1])
            if i+1<n:
                tmp -= min(v,grid[i+1][j])
            if j+1<n:
                tmp -= min(v,grid[i][j+1])
            res += tmp
print(res)