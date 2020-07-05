n = int(input())
li = []
for i in range(n):
    li.append([int(x) for x in input().split(",")])
dp = [[-10000 for x in range(n)] for x in range(n)]
dp[-1][-1] = max(0,-li[-1][-1])
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if i==n-1 and j<n-1:
            dp[i][j] = max(0,dp[i][j+1]-li[i][j])
        elif i<n-1 and j == n-1:
            dp[i][j] = max(0,dp[i+1][j]-li[i][j])
        elif i<n-1 and j<n-1:
            dp[i][j] = max(0,min(dp[i+1][j],dp[i][j+1])-li[i][j])
print(dp[0][0]+1)