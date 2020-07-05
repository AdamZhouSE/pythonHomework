t=int(input())
while(t>0):
    t-=1
    k=int(input())
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    dp=[[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,k+1):
            dp[i][j]=dp[i-1][j]
            for p in range(1,i): dp[i][j]=max(dp[i][j],dp[p-1][j-1]+arr[i-1]-arr[p-1])
    print(dp[n][k])