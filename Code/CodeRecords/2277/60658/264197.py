k = int(input())
n = int(input())
dp = [[-1 for i in range(k+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][1]=i
    dp[i][0]=0
for i in range(k+1):
    dp[0][i]=0
    dp[1][i]=1
for floor in range(2,n+1):
    for egg in range(2,k+1):
        temp = 0x3f3f3f3f
        for drop in range(floor+1):
            broken=dp[drop-1][k-1]
            unbroken = dp[floor-drop][k]
            temp = min(temp,1+max(broken,unbroken))
        dp[floor][egg]=temp
print(dp[n][k])