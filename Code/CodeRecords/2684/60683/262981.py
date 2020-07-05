T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [int(x) for x in input().split()]
    dp = [[[0, 0] for j in range(N)] for k in range(N)]
    p = N - 2
    dp[N - 1][N - 1][0] = nums[N - 1]
    while p >= 0:
        dp[p][N - 1][0] = min(dp[p + 1][N - 1][0], dp[p + 1][N - 1][1]) + nums[p]
        dp[p][N - 1][1] = dp[p + 1][N - 1][0]
        p -= 1
    print(min(dp[0][N - 1][0], dp[0][N - 1][1]))