def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        mark = [3, 5, 10]
        dp = [1 for i in range(n+1)]

        for i in range(3):
            for j in range(mark[i], n+1):
                dp[j] = dp[j] + dp[j-mark[i]]

    print(dp[n])

solve()