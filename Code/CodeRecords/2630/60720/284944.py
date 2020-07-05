list0=eval(input())
n=len(list0)
e= pow(n,2)
s=0
mid=(s+e)//2
visit=[[0 for i in range(n)]for j in range(n)]
def dfs(i,j):
    if visit[i][j]==1:
        return
    if list0[i][j]>mid:
        return
    visit[i][j]=1
    if i>0:
        dfs(i-1,j)
    if j>0:
        dfs(i,j-1)
    if i<n-1:
        dfs(i+1,j)
    if j<n-1:
        dfs(i,j+1)
while(s<e):
    visit = [[0 for i in range(n)] for j in range(n)]
    mid = (s + e) // 2
    dfs(0,0)
    if visit[n-1][n-1]==1:
        e=mid-1
    else:
        s=mid+1
print(s)