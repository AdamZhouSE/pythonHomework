E = []
n, m = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    E.append([u, v, w])
E.sort(key=lambda x: x[2])

fa = [i for i in range(n + 1)]

def find(x):
    global fa
    if x == fa[x]: return x
    fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    global fa
    x = find(x)
    y = find(y)
    fa[x] = y

cnt = 0
ans = 0

i = 0
while cnt < n - 1:
    e = E[i]
    if find(e[0]) != find(e[1]):
        ans += e[2]
        cnt += 1
        merge(e[0], e[1])
    i += 1

print(ans, end="")