def find(u):
    for v in table[u]:
        if not r_vis[v]:
            r_vis[v] = 1
            if right[v] == -1 or find(right[v]):
                left[u] = v
                right[v] = u
                return 1
    return 0


n, m = map(int, input().split())
nx, ny = m, n - m
left, right = [-1] * n, [-1] * n
table = [[] for _ in range(m)]
while True:
    try:
        a, b = map(int, input().split())
        table[a - 1].append(b - 1)
    except:
        break
ans = 0
for i in range(m):
    r_vis = [0] * n
    ans += find(i)
print(ans)