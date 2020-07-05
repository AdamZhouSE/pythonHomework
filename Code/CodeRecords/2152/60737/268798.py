n = 0
INF = 999999
orz = [0] * INF
d = [0] * INF
f = [0] * INF
ans = [0] * INF
vis = [0] * INF
que, stk = [], []


def top_sort():
    for i in range(1, n + 1):
        if not d[i]:
            que.append(i)
    while que:
        t = que.pop(0)
        stk.append(t)
        d[f[t]] -= 1
        if not d[f[t]]:
            que.append(f[t])


def dfs(u, root):
    if vis[u]:
        return
    vis[u] = 1
    ans[root] += orz[u]
    que.append(u)
    dfs(f[u], root)


def circle():
    for i in range(1, n + 1):
        if d[i] and not vis[i]:
            dfs(i, i)
            while que:
                t = que.pop(0)
                ans[t] = ans[i]


if __name__ == "__main__":
    n = int(input())
    l1 = [int(i) for i in input().split( )]
    for i in range(1, n+1):
        orz[i] = l1[i-1]
    l2 = [int(i) for i in input().split()]
    for i in range(1, n + 1):
        f[i] = l2[i - 1]
        d[f[i]] += 1
    top_sort()
    circle()
    while stk:
        t = stk.pop()
        ans[t] = orz[t] + ans[f[t]]
    for i in range(1, n + 1):
        print(ans[i])

 