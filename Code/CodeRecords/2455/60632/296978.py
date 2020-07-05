def dfs(x: int, fa: int):
    f[x] = a[x]
    for i in range(len(e[x])):
        t = e[x][i]
        if t != fa:
            dfs(t, x)
            if f[t] > 0:
                f[x] += f[t]


n = int(input())
f = [0 for i in range(n+1)]
ans = -2147483647
e = [[] for j in range(n+1)]
a = list(map(int, input().strip().split(' ')))
for i in range(n - 1):
    u, v = map(int, input().strip().split(' '))
    e[u-1].append(v-1)
    e[v-1].append(u-1)
dfs(1, 0)
for i in range(n):
    ans = max(ans, f[i])
print(ans,end='')
