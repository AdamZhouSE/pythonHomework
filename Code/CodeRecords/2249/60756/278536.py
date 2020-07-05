L=int(input())
grid=[]
ans=L*L
for i in range(L):
    x=list(map(int,input().split(",")))
    grid.append(x)
    ans-=x.count(0)
for i in range(L):
    ans+=max(grid[i])
    ans+=max(grid[j][i] for j in range(L))
print(ans)