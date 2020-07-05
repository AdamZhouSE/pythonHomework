s = input()
t = input()
k = int(input())
n = len(s)
m = len(t)
N = max(n, m) + 10
S = []
T = []
for i in list(s):
    S.append(ord(i))
for i in list(t):
    T.append(ord(i))
dp = [[0]*N for i in range(0, N)]
dp[0][0] = 0
for i in range(1, n+1):
    dp[i][0] = i * k
for i in range(1, m+1):
    dp[0][i] = i * k
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = min(dp[i - 1][j - 1] + abs(S[i - 1] - T[j - 1]), min(dp[i - 1][j], dp[i][j - 1]) + k)
print(dp[n][m], end='')