import math as m
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
dp = [1] * 60
for i in range(3, 60):
    dp[i] = 0
    for j in range(1, (i // 2) + 1):
        dp[i] = max(dp[i], max(dp[j], j) * max(dp[i - j], i - j))

print(dp[n])
