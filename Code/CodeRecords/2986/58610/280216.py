raw_s, tar_s = input(), input()
dp = [[0 for i in range(len(raw_s) + 1)] for j in range(len(tar_s) + 1)]
# dp = [([0] * (len(raw_s) + 1)) * (len(tar_s) + 1)]  # 构造(n+1)*(m+1)的dp矩阵
for i in range(len(raw_s) + 1):
    dp[0][i] = i
for i in range(len(tar_s) + 1):
    dp[i][0] = i
for i in range(1, len(tar_s) + 1):
    for j in range(1, len(raw_s) + 1):
        dp[i][j] = min(min(dp[i][j - 1] + 1, dp[i - 1][j] + 1),
                       dp[i - 1][j - 1] if raw_s[j - 1] == tar_s[i - 1] else dp[i - 1][j - 1] + 1)
print(dp[len(tar_s)][len(raw_s)])