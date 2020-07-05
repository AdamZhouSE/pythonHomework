inp = input().split(',')
n = len(inp)
res = 1

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if inp[i] > inp[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    res = max(res, dp[i])
print(res)
