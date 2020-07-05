s1 = input()
s2 = input()
space = int(input())
dp = [[0] * 2001 for i in range(2001)]
m, n = len(s1), len(s2)
for i in range(1, m + 1):
    dp[i][0] = dp[i - 1][0] + space
for j in range(1, n + 1):
    dp[0][j] = dp[0][j - 1] + space
for a in range(1, m + 1):
    for b in range(1, n + 1):
        dp[a][b] = min((dp[a - 1][b - 1] + abs(ord(s1[a - 1]) - ord(s2[b - 1]))), min(dp[a - 1][b] + space, dp[a][b - 1] + space))
print(str(dp[m][n]), end="")