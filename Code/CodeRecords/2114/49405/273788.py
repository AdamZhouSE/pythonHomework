n = int(input())
a = []
i = 1
while i * i <= n:
    a.append(i * i)
    i += 1
dp = [9999 for i in range(n + 1)]
dp[0] = 0
for i in range(1, n + 1):
    for c in a:
        if c > i: break
        dp[i] = min(dp[i], dp[i - c] + 1)
print(dp[n])