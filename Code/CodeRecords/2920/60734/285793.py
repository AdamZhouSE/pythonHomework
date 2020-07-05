import sys

lst = list(map(int, input().split(' ')))
n, part = lst[0], lst[1]
lst = list(map(int, input().split(' ')))
lst.insert(0,0)
dp = [[0 for i in range(part+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1, part+1):
        if i > j:
            dp[i][j] = sys.maxsize
            if j == 1:
                dp[i][j] = lst[i]-lst[1]
            else:
                for k in range(j-1, i):
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + lst[i]-lst[k+1])
print(dp[n][part])