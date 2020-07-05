s1 = input()
s2 = input()
m, n = len(s1), len(s2)
dp = [0] * (n + 1)
for j in range(1, n + 1):
    dp[j] = j
for i in range(1, m + 1):
    lt = dp[0]
    dp[0] = i
    for j in range(1, n + 1):
        up = dp[j]
        if s1[i - 1] == s2[j - 1]:
            dp[j] = lt
        else:
            dp[j] = min(up, dp[j - 1], lt) + 1
        lt = up
print(dp[n])