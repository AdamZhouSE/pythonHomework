def Islands(grid:list):
    nr = len(grid)
    nc = len(grid[0])
    num = 0
    for i in range(0,nr):
        for j in range(0,nc):
            if grid[i][j] =="1":
                num+=1
                dfs(grid,i,j)
    return num

def dfs(grid:list,r:int,c:int):
    nr = len(grid)
    nc = len(grid[0])
    if r<0 or r>=nr or c<0 or c>=nc :
        return
    if  grid[r][c]=="0":
        return

    grid[r][c] = "0"
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)
import sys
grid = []
for line in sys.stdin:
    # print(line)
    if line!=0 and line!="":
        grid.append(list(line))
    else:
        break
for i in range(len(grid)-1):
    grid[i] = grid[i][:-1]
# print(grid)
print(Islands(grid))
