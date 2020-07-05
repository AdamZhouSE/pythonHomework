t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    dp = [1 for i in range(n)]
    res = -1
    for i in range(n):
        for j in range(i):
            if s[j]<s[i]:
                dp[i]=max(dp[i],dp[j]+1)
        res = max(res,dp[i])
    print(res)