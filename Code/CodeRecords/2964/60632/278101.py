def val(x: str, y: str) -> int:
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    dp = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    for i in range(len(dp[0])):
        dp[0][i] = i
    for i in range(len(dp)):
        dp[i][0] = i
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            if x[i - 1] == y[j - 1]:
                tmp = 0
            else:
                tmp = 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + tmp)
    return dp[len(x)][len(y)]


n = int(input())
data = []
for i in range(n):
    data.append(input())
res = [0 for i in range(8)]
for i in range(len(res)):  # 统计相似度为i+1的字符串对数
    count = 0
    for j in range(n - 1):
        for k in range(j + 1, n):
            if val(data[j], data[k]) == i + 1:
                count += 1
    res[i] = count
print(*res, end=' ')
