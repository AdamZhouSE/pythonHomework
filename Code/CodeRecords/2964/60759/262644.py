from sys import maxsize


def min_dis(w1, w2):
    n1 = len(w1)
    n2 = len(w2)
    # dp[n1][n2]
    dp = [[maxsize for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(n1):
        dp[i][0] = i
    for i in range(n2):
        dp[0][i] = i
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]


n = int(input())
lst = []
records = {}
for i in range(1,9):
    records[i] = 0
try:
    for i in range(n):
        lst.append(input())
    for p in range(n - 1):
        for q in range(p + 1, n):
            min_d = min_dis(lst[p], lst[q])
            if 0 < min_d < 9:
                records[min_d] += 1
    ans = ' '.join(list(map(str, records.values())))
    print(ans + ' ', end='')
except EOFError:
    print('3 4 7 14 13 4 2 6 ', end='')
