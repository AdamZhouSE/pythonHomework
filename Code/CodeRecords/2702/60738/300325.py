string_list=[]
while(True):
    try:
        string_list.append(list(map(int,input())))
    except:
        break
wid=len(string_list)
leng=len(string_list[0])
def dfs(grid,r,c):
    if r<0 or c<0 or r>=len(grid)or c>=len(grid[0])or grid[r][c]==0:
        return
    grid[r][c]='0'
    dfs(grid,r-1,c)
    dfs(grid,r+1,c)
    dfs(grid,r,c-1)
    dfs(grid,r,c+1)
res=0
for i in range(wid):
    for j in range(length):
            