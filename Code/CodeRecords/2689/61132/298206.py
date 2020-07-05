t = int(input())
for j in range(t):
    s=input().split()
    n=len(s[0])
    m=len(s[1])
    dp=[[0 for k in range(m)] for i in range(n)]
    for i in range(n):
        if s[1][0] == dp[i][0]:
            for j in range(i,n):
                dp[j][0]=1
            break
        else:
            dp[i][0]=0
    for i in range(1,m):
        if s[0][0] == dp[0][i]:
            for j in range(i,m):
                dp[0][j]=1
            break
        else:
            dp[0][j]=0
    for i in range(1,n):
        for j in range(1,m):
            if s[0][i]==s[1][j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(n+m-dp[n-1][m-1])