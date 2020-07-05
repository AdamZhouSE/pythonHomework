n = int(input())
s = input()
m = len(s)
w = []
dp = []

for i in range(n):
    w.append(input())

for i in range(m + 1):
    dp.append(m * 2)

dp[0] = 0
for i in range(1, m + 1):
    for j in range(n):
        if i - 1 + len(w[j]) <= m:
            if w[j] == s[i:i+len(w[j])]:
                dp[i - 1 + len(w[j])] = min(dp[i - 1 + len(w[j])], dp[i] + 1)
if dp[m] == m * 2:
    print(-1)
else:
    print(dp[m])