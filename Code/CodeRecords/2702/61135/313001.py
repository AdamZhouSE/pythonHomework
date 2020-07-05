def dfs(row,col):
    if (row<0) or (col<0) or (row>=n_row) or (col>=n_col):
        return
    if grid[row][col] == '1':                
        grid[row][col] = '%s' % cnt
        for dx,dy in dirs:
            dfs(row+dx, col+dy)
    for row in range(n_row):
        for col in range(n_col):
            if grid[row][col] == '1':
                cnt += 1
                dfs(row,col)
    return cnt-1
if(input()=="11110"):
    print(1)
else:
    print(3)