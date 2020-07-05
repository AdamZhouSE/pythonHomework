T=int(input())
for k in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    sum1=sum(l[i] for i in range(n))
    dp=[[0]*(sum1//2+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,sum1//2+1):
            if j>=l[i-1]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i-1]]+l[i-1])
    print(sum1-2*dp[n][sum1//2])