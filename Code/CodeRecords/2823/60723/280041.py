num=input().split()
n=int(num[0])
m=int(num[1])
MOD=1000000007
dp=[[0 for _ in range(m)] for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=1
    for j in range(i,n+1,i):
        for k in range(1,m):
            dp[j][k]=dp[j][k]+dp[i][k-1]
            dp[j][k]=dp[j][k]%MOD
result=0
for i in range(1,n+1):
    result=result+dp[i][m-1]
print(result%MOD)