ts = int(input())
for t in range(ts):
    K, N = int(input()), int(input())
    prices = list(map(int, input().split(' ')))
    prices.insert(0, 0)
    # dp[i][k][s] 今天是第i天，至今为止进行了至多k次交易，是否有股票(s)
    dp = [[[0 for s in range(2)] for k in range(K + 1)] for i in range(N + 1)]
    for k in range(K + 1):
        dp[0][k][1] = -float('inf')
    for i in range(N + 1):
        dp[i][0][1] = -float('inf')
    for i in range(1, N + 1):
        for k in range(1, K + 1):
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    print(dp[N][K][0])
