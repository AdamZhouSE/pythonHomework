import sys


def dfs(i, k, res):
    visit[i] = k
    choosed[i] = True
    if not choosed[inner[i]]:
        res = dfs(inner[i], k + 1, res)
    if visit[inner[i]] != 0 and visit[inner[i]]-visit[i] != 1:
        res = min(res, visit[i] - visit[inner[i]] + 1)
    visit[i] = 0
    return res


sys.setrecursionlimit(100000067)
n = int(input())
inner = [int(i) - 1 for i in input().split()]
d = [0] * n
visit = [0] * n
choosed = [False] * n
gameNum = n
for i in range(0, n):
    if not choosed[i]:
        gameNum = dfs(i, 1, gameNum)
print(gameNum, end='')