def maxSubarr(A,B):
    dp = [[0]*len(B) for i in range(len(A))]
    res = 0
    for i in range(0,len(B)):
        if(A[0]==B[i]):
            dp[0][i]=1
    for i in range(0, len(A)):
        if (B[0] == A[i]):
            dp[i][0] = 1
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            if(A[i]==B[j]):
                dp[i][j] = dp[i-1][j-1] + 1
            res = max(dp[i][j],res)
    return res


temp = eval(input())
A= []
for t in temp:
    A.append(int(t))
temp = eval(input())
B= []
for t in temp:
    B.append(int(t))
print(maxSubarr(A,B))

