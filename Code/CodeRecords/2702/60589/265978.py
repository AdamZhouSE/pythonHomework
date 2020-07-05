from sys import stdin

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def num_islands():
    grids=stdin.readlines() #读取多行输入直至eof 结果为list list中各str带换行符
    for i in range(len(grids)):
        grids[i]=grids[i].strip()
        grids[i]=list(grids[i])
    m = len(grids)
    if m == 0:
        return 0
    n = len(grids[0])
    if n == 0:
        return 0
    visited=[[False]*n]*m
    cnt=0
    for i in range(m):
        for j in range(n):
            if grids[i][j]=='1' and visited[i][j]==False:
                cnt+=1
                dfs(grids,m,n,visited,i,j)
    return cnt


def dfs(grids,m,n,visited,i,j):
    visited[i][j]=True
    for direction in directions:
        i_2 = i + direction[0]
        j_2 = j + direction[1]
        if 0 <= i_2 < m and 0 <= j_2 < n and not visited[i_2][j_2] and grids[i_2][j_2] == '1':
            dfs(grids,m,n,visited,i_2,j_2)


print(num_islands())