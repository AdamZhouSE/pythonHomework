N=int(input())
grid=[]
ans=0
for i in range(N):
    grid.append(list(map(int,input().split(","))))
for i in range(N):
    for j in range(N):
        if grid[i][j]>0:
            ans+=(2+grid[i][j]*4)
            if i>0:
                ans-=min(grid[i][j],grid[i-1][j])*2
            if j>0:
                ans-=min(grid[i][j],grid[i][j-1])*2
print(ans)