n,m=map(int,input().split())
mp=[[0 for i in range(m)] for i in range(n)]
f=[[0 for i in range(m)] for i in range(n)]
dis=[[1,0],[-1,0],[0,1],[0,-1]]
def dfs(x,y,s):
    if s==0:#Bob
        cnt=1
        for i in range(4):
            xx=x+dis[i][0]
            yy=y+dis[i][1]
            if (xx<0 or xx>=n or yy<0 or yy>=m):
                continue
            if f[xx][yy] or mp[xx][yy]:
                continue
            f[xx][yy]=1
            cnt=cnt and dfs(xx,yy,1-s)
            f[xx][yy]=0
    else:#Alice
        cnt=0
        for i in range(4):
            xx=x+dis[i][0]
            yy=y+dis[i][1]
            if (xx<0 or xx>=n) or (yy<0 or yy>=m):
                continue
            if f[xx][yy] or mp[xx][yy]:
                continue
            f[xx][yy]=1
            cnt=cnt or dfs(xx,yy,1-s)
            f[xx][yy]=0
    return cnt
for i in range(n):
    s=input()
    for j in range(m):
        mp[i][j]=0 if s[j]=='.' else 1
res=[]
for i in range(n):
    for j in range(m):
        if  mp[i][j]==0:
            f[i][j]=1
            if dfs(i,j,0)==1:
                res.append((i+1,j+1))
            f[i][j]=0
print(len(res))
for item in res:
    print(item[0],item[1])