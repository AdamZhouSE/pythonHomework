t = int(input())
for _ in range(t):
    xs = input()
    n = len(xs)
    dp = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    cnt = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            dp[i][j] = dp[i - 1][j]
            v = int(xs[i - 1])
            dp[i][j][v] = dp[i][j][v] + 1
            check = lambda i, j: dp[i][j][0] == dp[i][j][1] and dp[i][j][0] == dp[i][j][2]
            if check(i, j):
                cnt += 1
    print(cnt)
