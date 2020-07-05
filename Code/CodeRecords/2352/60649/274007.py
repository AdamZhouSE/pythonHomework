N,M,Q=map(int,input().split())
mat=[]
nex=((0,-1),(0,1),(1,0),(-1,0))
def dfs(x,y):
    global xi1,yi1,xi2,yi2
    tmpmat[x][y]=0
    for i in range(4):
        nx=x+nex[i][0]
        ny=y+nex[i][1]
        if 0<=nx<=xi2-xi1 and 0<=ny<=yi2-yi1 and tmpmat[nx][ny]==1:
            dfs(nx,ny)
for i in range(N):
    mat.append(list(map(int,list(input()))))
for q in range(Q):
    xi1,yi1,xi2,yi2=map(int,input().split())
    tmpmat=mat[xi1-1:xi2]
    tmpmat=[m[yi1-1:yi2] for m in tmpmat]
    res=0
    for i in range(xi2-xi1+1):
        for j in range(yi2-yi1+1):
            if tmpmat[i][j]==1:
                dfs(i,j)
                res+=1
    print(res)
