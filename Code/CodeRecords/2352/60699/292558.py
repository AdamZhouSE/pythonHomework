list1=list(map(int,input().split(' ')))
m=list1[0]
n=list1[1]
q=list1[2]
grid=[]
for i in range(m):
    temp=input()
    cur=[]
    for j in temp:
        cur.append(int(j))
    grid.append(cur)
for i in range(q):
    list2=list(map(int,input().split(' ')))
    x1=list2[0]
    y1=list2[1]
    x2=list2[2]
    y2=list2[3]
    grid_temp=[]
    for i in range(x1,x2+1):
        t=[]
        for j in range(y1,y2+1):
            t.append(grid[i-1][j-1])
        grid_temp.append(t)
    cur=0
    def dfs(grid,start_x,start_y,lenx,leny):
        grid[start_x][start_y]=0
        if start_x-1>=0 and grid[start_x-1][start_y]==1:
            dfs(grid,start_x-1,start_y,lenx,leny)
        if start_y-1>=0 and grid[start_x][start_y-1]==1:
            dfs(grid,start_x,start_y-1,lenx,leny)
        if start_x+1<lenx and grid[start_x+1][start_y]==1:
            dfs(grid,start_x+1,start_y,lenx,leny)
        if start_y+1<leny and grid[start_x][start_y+1]==1:
            dfs(grid,start_x,start_y+1,lenx,leny)
    def containsOne(grid):
        x=len(grid)
        y=len(grid[0])
        for i in range(x):
            for j in range(y):
                if grid[i][j]==1:
                    return True
        return False
    while containsOne(grid_temp):
        x = len(grid_temp)
        y = len(grid_temp[0])
        for i in range(x):
            for j in range(y):
                if grid_temp[i][j] == 1:
                    dfs(grid_temp,i,j,x,y)
                    cur+=1
    print(cur)