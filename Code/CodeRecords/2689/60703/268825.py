def superSeq(X,Y,m,n):
    dp = [[0]*(n+2) for i in range(m+2)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0):
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif X[i-1] ==Y[j-1]: #后面的越早消掉越好
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j])
    return dp[m][n]
T =int(input())
for i in range(T):
    strList = input().split()
    X,Y = strList[0],strList[1]
    m = len(X)
    n = len(Y)
    print(superSeq(X,Y,m,n))