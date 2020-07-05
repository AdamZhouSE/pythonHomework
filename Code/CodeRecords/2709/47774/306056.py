grid=eval(input())
hits=eval(input())
def dfs(grid,i,j):
    if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
        return 0
    grid[i][j] = 2;
    return dfs(grid,i+1,j)+dfs(grid,i-1,j)+dfs(grid,i,j-1)+dfs(grid,i,j+1)+1

res=[0 for i in range(len(hits))]
def hit(grid,hits):
    m=len(grid)
    n=len(grid[0])
    for i in range(len(hits)):
        grid[hits[i][0]][hits[i][1]]-=1
    for i in range(n):
        if grid[0][i]==1:
            dfs(grid,0,i)
    for i in range(len(hits)-1,-1,-1):
        x=hits[i][0]
        y=hits[i][1]
        grid[x][y]+=1
        if grid[x][y]==1:
            if (x-1>=0 and grid[x-1][y]==2) or (x+1<m and grid[x+1][y]==2) or (y-1>=0 and grid[x][y-1]==2) or (y+1<n and grid[x][y+1]==2) or x==0:
                res[i]=dfs(grid,x,y)-1
    return res

print(res)
     
