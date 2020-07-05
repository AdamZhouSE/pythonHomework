import sys
def dfs(i,j,center_v,M,dp,rows,cols):
    if i<0 or i>=rows or j<0 or j>=cols:
           return 0
    if M[i][j]<=center_v:
        return 0
    if dp[i][j]==-1:
        nd=[]
        nd.append((i-1,j))
        nd.append((i+1,j))
        nd.append((i,j-1))
        nd.append((i,j+1))
        max_p=-sys.maxsize
        for x,y in nd:
            max_p=max(max_p,dfs(x,y,M[i][j],M,dp,rows,cols))
        dp[i][j]=max_p+1
    return dp[i][j]
def longestIncreasingPath(M):
    if not MemoryError:
        return 0
    rows=len(M)
    cols=len(M[0])
    dp=[[-1]*cols for _ in range(rows)]
    max_p=-sys.maxsize
    for i in range(rows):
        for j in range(cols):
            max_p=max(max_p,dfs(i=i,j=j,center_v=M[i][j]-1,M=M,dp=dp,rows=rows,cols=cols))
    return max_p



s=''
while True:
    a=input()
    if a!=']':
        s=s+a
    else:
        break
s=s+a
A=eval(s)
print(longestIncreasingPath(A))
