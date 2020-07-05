import sys


def dfs(i, k, res):
    visit[i] = k
    choosed[i] = 1
    if choosed[inner[i]] == 0:
        res = dfs(inner[i], k + 1, res)
    if visit[inner[i]] != 0 and visit[i] - visit[inner[i]] + 1 != 0:
        res = min(res, visit[i] - visit[inner[i]] + 1)
    visit[i] = 0
    return res


sys.setrecursionlimit(10000000)
n = int(input())
inner = [int(i) - 1 for i in input().split()]
d = [0] * n
visit = [0] * n
choosed = [0] * n
gameNum = n
for i in range(0, n):
    if choosed[i] == 0:
        gameNum = dfs(i, 1, gameNum)
print(gameNum, end='')