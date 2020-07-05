import re
def ad(x, y):
    global cnt
    global next
    global to
    global head
    cnt += 1
    next[cnt] = head[x]
    to[cnt] = y
    head[x] = cnt


def dfs(u, fa):
    global head
    global next
    global to
    global f
    global ans
    f[u] = a[u]
    i = head[u]
    flag = True
    while flag:
        v = to[i]
        if v != fa:
            dfs(v, u)
            f[u] += max(0, f[v])
        i = next[i]
        if i <= 0:
            flag = False
    ans = max(ans, f[u])


if __name__ == '__main__':
    next = [0]*1000
    to = [0]*1000
    f = [0]*1000
    head = [0]*1000
    ans = 0
    cnt = 0
    n = int(input())
    a = list([int(n) for n in re.findall(r"\-?\d+", input())])
    a.insert(0, 0)
    for i in range(1, n):
        s = list([int(n) for n in re.findall(r"\-?\d+", input())])
        x = s[0]
        y = s[1]
        ad(x, y)
        ad(y, x)
    dfs(1, 0)
    print(ans, end='')