import sys


def dfs(i, k, res=sys.maxsize):
    visit[i] = k
    chosen[i] = True
    if not chosen[inner[i]]:
        res = dfs(inner[i], k + 1, res)
    if visit[inner[i]] != 0 and visit[inner[i]] - visit[i] != 1:
        res = min(res, visit[i] - visit[inner[i]] + 1)
    visit[i] = 0
    return res


sys.setrecursionlimit(int(sys.maxsize / 6766666666))
n = int(input())
inner = [int(i) - 1 for i in input().split()]
d = [0] * n
visit = [0] * n
chosen = [False] * n
print(min([dfs(i, 1) for i in range(n) if not chosen[i]]), end='')