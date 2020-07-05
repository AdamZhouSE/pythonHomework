list1=list(map(int,input().split(",")))
coins=[1]+list1+[1]
dp=[[0 for j in range(len(coins))] for i in range(len(coins))]
for i in range(2,len(coins)):
    for j in range(0,len(coins)-i):
        for k in range(j+1,j+i):
            dp[j][j+i]=max(dp[j][j+i],dp[j][k]+dp[k][j+i]+coins[j]*coins[k]*coins[j+i])
print(dp[0][len(coins)-1])