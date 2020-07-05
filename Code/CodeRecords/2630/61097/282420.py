import re

def dfs(x,y,hei,n):
    if(vis[x][y]==1): return
    if(grid[x][y]>hei): return
    vis[x][y]=1
    if(x>0): dfs(x-1,y,hei,n)
    if(x<n-1): dfs(x+1,y,hei,n)
    if(y>0): dfs(x,y-1,hei,n)
    if(y<n-1): dfs(x,y+1,hei,n)

str=input()
arr=re.findall(r'\d+',str)
size=len(arr)
n=int(size**0.5)
grid=[[0 for i in range(n)]for j in range(n)]
left=5000
right=0
for i in range(n):
    for j in range(n):
        grid[i][j]=int(arr[i*n+j])
        right=max(right,grid[i][j])
        left=min(left,grid[i][j])
#print(arr)
#print(grid)
#print(left,right)
ans=5000
while left<=right:
    mid=int((left+right)/2)
    vis=[[0 for i in range(n)] for j in range(n)]
    dfs(0,0,mid,n)
    if(vis[n-1][n-1]==1):
        ans=min(ans,mid)
        right=mid-1
    else: left=mid+1
print(ans) 
