def dp(x):
    global son
    global f
    global h
    f[x][0] = 0
    f[x][1] = h[x]
    for i in range(0, len(son[x])):
        y = son[x][i]
        dp(y)
        f[x][0] += max(f[y][0], f[y][1])
        f[x][1] += f[y][0]


if __name__ == '__main__':
    h = [0]*1000
    v = [0]*1000
    f = [[0]*2 for i in range(0, 1000)]
    son = [[] for i in range(0, 1000)]
    n = int(input())
    for i in range(1, n+1):
        h[i] = int(input())
    for i in range(0, n):
        x, y = map(int, input().split(' '))
        son[y].append(x)
        v[x] = 1
    root = 0
    for i in range(1, n+1):
        if v[i] == 0:
            root = i
            break
    dp(root)
    print(max(f[root][0], f[root][1]), end='')