s = input()
t = input()
n, m = map(len, (s, t))
s = " " + s
t = " " + t
dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i] == t[j]: dp[i][j] = dp[i - 1][j - 1] + 1
        else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        ans = max(ans, dp[i][j])
print(ans == n)