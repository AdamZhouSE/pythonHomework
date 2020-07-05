n=int(input())
dp=[i for i in range(n)]
dp.append(1)
for i in range(2,n+1):
    for j in range(1,i//2+1):
        dp[i]=max(dp[i],dp[j]*dp[i-j])
print(dp[-1])