#树形dp

from collections import defaultdict

nq=input().split(' ')
n=int(nq[0])
q=int(nq[1])
son=defaultdict(list)
f=[[0 for i in range(109)] for j in range(109)]
val=[[0 for i in range(109)] for j in range(109)]
used=[0]*109
for i in range(n-1):
    abc=input().split(' ')
    a=int(abc[0])
    b=int(abc[1])
    c=int(abc[2])
    val[a][b]=c
    val[b][a]=c
    son[a].append(b)
    son[b].append(a)


def dfs(x):
    used[x]=1
    for i in range(len(son[x])):
        ny=son[x][i]
        if used[ny]==1:
            continue
        used[ny]=1
        dfs(ny)
        for j in range(q,0,-1):
            for k in range(j-1,-1,-1):
                f[x][j]=max(f[x][j],val[x][ny]+f[ny][k]+f[x][j-k-1])


dfs(1)
print(f[1][q])