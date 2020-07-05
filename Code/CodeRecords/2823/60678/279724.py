nAndK = input().split()
n = int(nAndK[0])
k = int(nAndK[1])
sum = 0
mod = 1000000007
dp = []
for i in range(0, 2020):
    dp.append([0] * 2020)
for i in range(0, 2020):
    dp[1][i] = 1

for i in range(1, 2020):
    for j in range(1, 2020):
        for q in range(j, 2020, j):
            dp[i][q] += dp[i - 1][j]
            dp[i][q] %= mod

for i in range(1, n + 1):
    sum += dp[k][i]
    sum %= mod

print(sum)