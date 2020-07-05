n = int(input())
arr = [int(x) for x in input().split(" ")]
dp = []
for _ in range(n):
    dp.append([n,n,n])
if arr[0]==0:dp[0][0]=1
if arr[0]==1:dp[0][1]=0
if arr[0]==2:dp[0][2]=0
if arr[0]==3:dp[0][1]=dp[0][2]=0
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
    if arr[i] == 1 or arr[i] == 3:
        dp[i][1]=min(dp[i-1][0],dp[i-1][2],dp[i-1][1]+1)
    if arr[i] == 2 or arr[i] == 3:
        dp[i][2]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2]+1)
print(min(min(dp[n-1][0],dp[n-1][1]),dp[n-1][2]))