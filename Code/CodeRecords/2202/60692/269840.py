num = int(input())


def dfs(i, j, state, next):
    if j == 2:
        dp[i + 1][next] += dp[i][state]
        return
    if (1 << j) & state > 0:
        dfs(i, j + 1, state, next)
    if (1 << j) & state == 0:
        dfs(i, j + 1, state, next | (1 << j))
    if j + 1 < 2 and (1 << j) & state == 0 and (1 << (j + 1)) & state == 0:
        dfs(i, j + 2, state, next)
    return


res = []
for l in range(num):
    n = int(input())
    dp = [[0] * (1 << 2) for m in range(n + 1)]
    dp[0][0] = 1
    for h in range(n):
        for k in range(1 << 2):
            if dp[h][k]:
                dfs(h, 0, k, 0)
    res.append(dp[n][0])
for a in res:
    print(a)