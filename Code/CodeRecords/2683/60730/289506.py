num = int(input())
for i in range(num):
    m = list(input())
    res = 0
    dp = [1] * len(m)
    for j in range(len(m)):
        for k in range(j):
            if m[j] > m[k]:
                dp[j] = max(dp[j], dp[k] + 1)

        res = max(res, dp[j])

    print(res)
