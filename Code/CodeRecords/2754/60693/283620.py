def find_distance(mapp:[[int]]):
    n=len(mapp)
    dp=[[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if mapp[i][j]==1:
                dp[i][j]=0

    for i in range(n):
        for j in range(n):
            if mapp[i][j]==1:continue
            if i-1>=0:
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j])
            if j-1>=0:
                dp[i][j]=min(dp[i][j],dp[i][j-1]+1)

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if mapp[i][j]:continue
            if i+1<n:
                dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
            if j+1<n:
                dp[i][j]=min(dp[i][j],dp[i][j+1]+1)

    res=-1
    for i in range(n):
        for j in range(n):
            if not mapp[i][j]:
                res=max(res,dp[i][j])
                
    if res==float('inf'):return -1
    else:return res


mapp=eval(input())
print(find_distance(mapp))