temp=[int(x) for x in input().split()]
n=temp[0]
grid=[[0 for i in range(n)] for j in range(n)]

for i in range(temp[1]):
    te=[int(x)-1 for x in input().split()]
    grid[te[1]][te[0]]=1

visited=[False for i in range(n)]
def dfs(i):
    global visited
    visited[i]=True
    for j in range(n):
        if visited[j]==False and grid[i][j]==1:
            dfs(j)
total=0
for i in range(n):
    visited = [False for i in range(n)]
    visited[i]=True
    ans=0
    for j in range(n):
        if i!=j and grid[i][j]==1 and visited[j]==False:
            dfs(j)
    for k in visited:
        if k:
            ans+=1
    if ans==n:
        total+=1
print(total)
