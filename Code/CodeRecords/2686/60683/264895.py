T = eval(input())
for i in range(T):
    K = eval(input())
    N = eval(input())
    prices = [int(x) for x in input().split()]
    dp = [[[0, 0] for j in range(K + 1)] for k in range(N)]
    for j in range(N):
        for k in range(1, K + 1):
            if j - 1 == -1:
                # dp[j][k][0] = 0
                dp[j][k][1] = -prices[j]
            else:
                dp[j][k][0] = max(dp[j - 1][k][0], dp[j - 1][k][1] + prices[j])
                dp[j][k][1] = max(dp[j - 1][k][1], dp[j - 1][k - 1][0] - prices[j])
    print(dp[N - 1][K][0])