# 求交点最小个数
def reverse(l, n):
    for i in range(0, n // 2):
        l[i], l[n - 1 - i] = l[n - 1 - i], l[i]


def dfs(x, S, tot):
    global ans
    global cnt
    global m
    global b
    global c
    global st
    if tot >= ans:
        return
    if x == m:
        ans = tot
        return
    s = cnt[st[x] & S]
    dfs(x + 1, S | (1 << x), tot + min(s, b[x] - s))
    if x:
        dfs(x + 1, S, tot + min(c[x] - s, b[x] - c[x] + s))


t = int(input())
cnt = [0] * (1 << 22)
for i in range(1, 1 << 22):
    cnt[i] = cnt[i >> 1] + (i & 1)
for _ in range(1, t + 1):
    m = 0
    ans = 10000
    n = int(input())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    st = [0] * (n + 1)
    last = [0] * (n + 1)
    station = [int(i) for i in input().split(" ")]
    station.insert(0, 0)
    for i in range(1, n + 1):
        last[i] = 0
        b[i] = 0
        c[i] = 0
        st[i] = 0
    for i in range(n, 0, -1):
        if not last[station[i]]:
            last[station[i]] = i
        else:
            l[m] = i
            r[m] = last[station[i]]
            m += 1
    reverse(l, m)
    reverse(r, m)
    for i in range(m):
        for j in range(i):
            if r[j] > l[i]:
                b[i] += 1
                if r[j] < r[i]:
                    st[i] = st[i] | (1 << j)
                    c[i] += 1
    dfs(0,0,0)
    print(ans)
