T = int(input())
for t in range(T):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp = [[0, 0] for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = dp[i - 1][0] + a[i]
    print(max(dp[n]))