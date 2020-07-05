K, N, m = int(input()), int(input()), 0
dp = [[0 for i in range(N + 1)] for j in range(K + 1)]
while dp[K][m] < N:
    m += 1
    for i in range(1, K + 1):
        # print(m, dp)
        dp[i][m] = dp[i - 1][m - 1] + dp[i][m - 1] + 1
print(m)
