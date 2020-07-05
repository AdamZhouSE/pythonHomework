ns = int(input())
lst = []
for n in range(ns):
    lst.append(list(map(int, input().split(','))))
x, y = 0, 0
dp = [[0 for j in range(ns + 1)] for i in range(ns + 1)]
for i in range(ns + 1):
    dp[i][ns] = float('inf')
for j in range(ns + 1):
    dp[ns][j] = float('inf')
for i in range(ns - 1, -1, -1):
    for j in range(ns - 1, -1, -1):
        if (i, j) == (ns - 1, ns - 1):
            dp[ns - 1][ns - 1] = max(1, 1 - lst[ns - 1][ns - 1])
            continue
        dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - lst[i][j])
print(dp[0][0])
