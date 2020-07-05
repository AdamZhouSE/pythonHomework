n = int(input())
p = int(1e9+7)
if n<2:
    print(1)
else:
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j - 1] * dp[i - j]
    print(dp[n]%p)
