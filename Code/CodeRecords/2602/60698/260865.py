# 12
a = list(eval(input()))
b = list(eval(input()))
length=0
dp = [[0] * len(b) for _ in range(0, len(a))]
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            try:
                dp[i][j] = dp[i - 1][j - 1] + 1
            except:
                dp[i][j] = 1
            if length<dp[i][j]:
                length=dp[i][j]
print(length)
