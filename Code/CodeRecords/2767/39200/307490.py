t = int(input())
for x in range(t):
    n = int(input())
    dp = []
    for i in range(n + 1):
        dp.append(0)
    dp[0] = 1
    for i in range(3, n + 1):
        dp[i] += dp [i-3]
    for i in range(5, n + 1):
        dp[i] += dp [i-5]
    for i in range(10, n + 1):
        dp[i] += dp [i-10]
    print(dp[n])
