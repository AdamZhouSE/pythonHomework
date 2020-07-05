def maxDistance(grid):
    n=len(grid)
    queue=[(i,j) for i in range(n) for j in range(n) if grid[i][j]==1]
    if len(queue)==n*n or  not queue:
        return -1
    level=0
    while queue:
        t=[]
        for x,y in queue:
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<n and 0<=j<n and grid[i][j]==0:
                    t.append((i,j))
                    grid[i][j]=1
        queue=t
        level+=1
    return level-1
    
grid=input()
level=maxDistance(grid)
print(level)