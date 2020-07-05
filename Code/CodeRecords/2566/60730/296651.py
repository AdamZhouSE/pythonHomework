num = int(input())
m = []
for i in range(num):
    m.append(list(map(int, input().split(","))))
a = num
b = len(m[0])
dp = [[0] * b for _ in range(a)]
dp[-1][-1] = max(1, 1 - m[-1][-1])
for i in range(b - 2, -1, -1):
    dp[-1][i] = max(1, dp[-1][i + 1] - m[-1][i])
for i in range(a - 2, -1, -1):
    dp[i][-1] = max(1, dp[i + 1][-1] - m[i][-1])
for i in range(a - 2, -1, -1):
    for j in range(b - 2, -1, -1):
        dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - m[i][j], 1)
print(dp[0][0])