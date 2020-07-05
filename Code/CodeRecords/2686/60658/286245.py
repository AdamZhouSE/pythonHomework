def dfs(k,n):
    if k==0 or n<0:
        return 0
    if dp[k][n]!=-1:
        return dp[k][n]
    ans = 0
    t1 = dfs(k,n-1)
    t2 = 0
    for i in range(n):
        t2 = max(t2,(arr[n]-arr[i])+dfs(k-1,i))
    ans = max(t1,t2)
    dp[k][n]=ans
#    for i in dp:
#        print(i)
#    print()
    return dp[k][n]