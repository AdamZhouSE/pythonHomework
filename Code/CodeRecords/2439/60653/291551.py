def ad(x, y, z):
    global to
    global next
    global w
    global cnt
    global last
    cnt += 1
    to[cnt] = y
    w[cnt] = z
    next[cnt] = last[x]
    last[x] = cnt


def dfs(x, deep, fa):
    global dep
    global len
    global to
    global next
    global w
    dep[x] = deep
    flag = True
    i = last[x]
    while flag:
        tt = to[i]
        if tt != fa:
            len[tt] = len[x]^w[i]
            dfs(tt, deep+1, x)
        i = next[i]
        if i <= 0:
            flag = False


if __name__ == '__main__':
    n = int(input())
    to = [0]*1000
    next = [0]*1000
    w = [0]*1000
    last = [0]*1000
    dep = [0]*1000
    len = [0]*1000
    size = [0]
    cnt = 0
    root = 1

    for i in range(0, n):
        size.append(1)
    for i in range(0, n-1):
        x, y, z = map(int, input().split(' '))
        ad(x, y, z)
        ad(y, x, z)
    dfs(1, 1, -1)
    m = int(input())
    for i in range(0, m):
        x, y = map(int, input().split(' '))
        print(len[x]^len[y])