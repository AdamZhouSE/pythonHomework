n,k=map(int,input().split())#最大值为n 长度为k
dp=[[0]*(n+1) for i in range(k+1)]
res=0
for i in range(1,n+1):
    dp[1][i]=1
for i in range(1,k):
    for j in range(1,n+1):
        for t in range(1,n//j+1):
            dp[i+1][j*t]+=dp[i][j]
            dp[i+1][j*t]%=1000000007
for i in range(1,n+1):
    res+=dp[k][i]
res%=1000000007
print(res)
