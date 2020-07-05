dp = [1]
n = int(input())
for i in range(n):
    temp = 0
    for j in range(i + 1):
        temp += dp[j] * dp[i - j]
    dp.append(temp)
print(dp[-1] % (10 ** 9 + 7))
