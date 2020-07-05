def maxDistance(grid,n) -> int:
    if grid==[[0]*n for _ in range(n)] or grid==[[1]*n for _ in range(n)]:
        return -1
    q = []
    loc=[-1,-1]
    #将陆地坐标位置加入队列
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                q.append([i, j])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        loc = q.pop(0)#陆地的坐标位置
        x, y = loc[0], loc[1]
        for off_x,off_y in zip(dx,dy):
            new_x, new_y = off_x + x, off_y + y
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or grid[new_x][new_y]!=0:
                continue
            #若朝当前陆地的某个方向前进，且目的地是海洋的，把它占领成陆地，将目的地位置上的数字加1，代表前进1（也就是距离加1）
            grid[new_x][new_y] = grid[x][y] + 1
            q.append([new_x, new_y])
    return grid[loc[0]][loc[1]] - 1


if __name__=="__main__":
    grid=eval(input())
    n=len(grid)
    ans=maxDistance(grid,n)
    print(ans)