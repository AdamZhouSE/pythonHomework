def findAndSet(grid,level):
    cnt=0
    for n, m in level:
        for x_off, y_off in (1, 0), (-1, 0), (0, 1), (0, -1):
            x = n + x_off
            y = m + y_off
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            else:
                if grid[x][y] == 1:
                    level.append([x, y])
                    grid[x][y] = 2
                    cnt+=1
    return grid, level, cnt


def init(grid,hits):
    for p in hits:
        i = p[0]
        j = p[1]
        if grid[i][j] == 1:
            grid[i][j] = -1
    #先把触顶的砖块值改为2
    level = []
    for k in range(len(grid)):
        if grid[0][k] == 1:
            level.append([0, k])
            grid[0][k] = 2
    #寻找最后仍能保持不落下的砖块，并将其标记改为2
    for n, m in level:
        for x_off, y_off in (1, 0), (-1, 0), (0, 1), (0, -1):
            x = n + x_off
            y = m + y_off
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                continue
            else:
                if grid[x][y] == 2:
                    level.append([x, y])
    #
    res=[]
    level=[]
    hits=list(reversed(hits))
    for ht in hits:
        n,m=ht[0],ht[1]
        if grid[n][m]==0:
            continue
        else:
            grid[n][m] = 2
            level.append([n, m])
            grid, level, cnt = findAndSet(grid, level)
            res.append(cnt)
    return res

if __name__=="__main__":
    grid=eval(input())
    hits=eval(input())
    ans=init(grid,hits)
    print(ans)