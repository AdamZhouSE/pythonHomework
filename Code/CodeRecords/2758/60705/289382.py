[n, m] = list(map(int, input().split(" ")))
f = [[0] * 135] * 135
dp = [0] * 135

for i in range(1, n+1):
    f = [[0] * 135] * 135
    f[0][1] = 1
    dp[0] = 1
    for j in range(1, m+1):
        for k in range(1, i+1):
            for l in range(0, k):
                f[j][k] += (dp[l] * f[j - 1][k - l]) % 10007
                f[j][k] %= 10007
    dp[i] = f[m][i]
print(dp[n])
