def change(x:str)->int:
    if x=='*':
        return 0
    else:
        return int(x)

N,M=map(int,input().split())
grid=[]
visited=[[0 for i in range(M+1)] for j in range(N+1)]
d=[(0,1),(1,0)]
ans=0
for i in range(N):
    row=list(map(change,list(input())))
    row.append(0)
    grid.append(row)
grid.append([0 for i in range(M+1)])
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            if grid[i][j]==2:
                visited[i][j]=1
                ans+=1
            else:
                for (x,y) in d:
                    if visited[i+x][j+y]==0 and grid[i][j]+grid[i+x][j+y]==4:
                        visited[i][j]=1
                        visited[i+x][j+y]=1
                        ans+=1
                        break
print(ans)