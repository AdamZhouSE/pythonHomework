def dfs(x:int):
    used[x]=1
    for i in range(len(son[x])):
        ny=son[x][i]
        if used[ny]==1:
            continue
        used[ny]=1
        dfs(ny)
        for j in range(q, 0, -1):
            for k in range(j-1, -1, -1):
                f[x][j] = max(f[x][j],val[x][ny]+f[ny][k]+f[x][j-k-1])


n, q = map(int, input().split(' '))
val = [[0 for i in range(109)] for j in range(109)]
f = [[0 for i in range(109)] for j in range(109)]
used = [0 for i in range(109)]
son = [[] for i in range(109)]
for i in range(n-1):
    a,b,c = map(int,input().split(' '))
    val[a][b] = c
    val[b][a] = c
    son[a].append(b)
    son[b].append(a)
dfs(1)
print(f[1][q])
