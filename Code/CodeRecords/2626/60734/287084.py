lst = list(map(int, input().split(',')))
n = len(lst)
lst.append(1)
lst.insert(0, 1)

dp = [[0 for i in range(n+2)] for j in range(n+2)]
for l in range(1, n+1):
    for i in range(1, n-l+2):
        j = i+l-1
        for k in range(i, j+1):
            dp[i][j] = max(dp[i][j], lst[i-1]*lst[k]*lst[j+1] + dp[i][k-1] + dp[k+1][j])
print(dp[1][n])