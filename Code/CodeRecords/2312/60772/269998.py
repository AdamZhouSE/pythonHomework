n = int(input())
mod = 1000000007

dp = [0] * (n + 1)
dp[0] = dp[1] = 1
for i in range(2, n + 1):
    for j in range(0, i):
        dp[i] += ((dp[j] % mod) * (dp[i - j - 1] % mod))
        dp[i] %= mod
print(dp[n])
