def dfs(u: int, fa: int):
    f[u] = a[u]
    for i in range(len(e[u])):
        t = e[u][i]
        if t != fa:
            dfs(t, u)
            if f[t] > 0:
                f[u] += f[t]


n = int(input())
f = [0 for i in range(16005)]
ans = -2147483647
e = [[] for j in range(16005)]
s = input()
a = []
try:
    a = list(map(int, s.strip().split(' ')))
except ValueError as e:
    print(s)
for i in range(n - 1):
    u, v = map(int, input().split(' '))
    e[u].append(v)
    e[v].append(u)
dfs(1, 0)
for i in range(n):
    ans = max(ans, f[i])
print(ans)
