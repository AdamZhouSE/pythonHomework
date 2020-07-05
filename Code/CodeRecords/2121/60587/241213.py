n = int(input())
if n == 1:
    res = 10
elif n > 10:
    res = 8877691
else:
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        if i < 3:
            dp[i] = dp[i - 1] * 9
        else:
            dp[i] = dp[i - 1] * (10 - i + 1)
    res = sum(dp)
print(res)