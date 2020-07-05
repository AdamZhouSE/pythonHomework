def build(a: int, b: int):
    ne[a][cnt[a]] = b
    cnt[a] += 1
    ne[b][cnt[b]] = a
    cnt[b] += 1


def dp(now: int, a: int, b: int):  # now为当前节点的值，b为父亲的值，a为另一边界
    fa = 0
    while ne[now][fa] != b:
        fa += 1  # 寻找父亲是相邻的第几个点
    if f[now][fa][a]:
        return f[now][fa][a]
    x, y, l, r = (0, 0, 0, 0)
    if a > b:
        x = b + 1
        y = a
    else:
        x = a
        y = b - 1
    for i in range(3):
        if i != fa and x <= ne[now][i] <= y:
            if ne[now][i] < now:
                l = max(l, dp(ne[now][i], x, now))
            else:
                r = max(r, dp(ne[now][i], y, now))
    f[now][fa][a] = l + r + 1
    return f[now][fa][a]


if __name__ == '__main__':
    n = eval(input())
    ans = 0
    ne = [[0, 0, 0] for i in range(1300)]
    cnt = [0 for i in range(1300)]
    f = [[[0 for k in range(1300)] for j in range(3)] for i in range(1300)]
    s = [[[0 for k in range(50)] for j in range(20)] for i in range(5)]
    for i in range(1, 5):
        for j in range(1, n+1):
            for k in range(1, 2 * j):
                s[i][j][k] = eval(input())
    for i in range(1, 5):
        for j in range(2, n + 1):
            for k in range(2, j << 1, 2):
                build(s[i][j][k], s[i][j-1][k-1])
                build(s[i][j][k], s[i][j][k-1])
                build(s[i][j][k], s[i][j][k+1])
    for i in range(1, n + 1):
        build(s[1][i][1], s[3][i][(i << 1)-1])
        build(s[2][i][1], s[1][i][(i << 1)-1])
        build(s[3][i][1], s[2][i][(i << 1)-1])
        build(s[4][i][1], s[1][n][2*n-(i << 1)+1])
        build(s[4][i][(i << 1)-1], s[2][n][(i << 1)-1])
        build(s[4][n][(i << 1)-1], s[3][n][2*n-(i << 1)+1])
    # 建边
    for i in range(1, 4 * n * n):  # 枚举根
        l = 0
        r = 0  # 记录最大左右子树
        for j in range(3):
            if ne[i][j] < i:
                l = max(l, dp(ne[i][j], 1, i))
            else:
                r = max(r, dp(ne[i][j], 4*n*n, i))
        ans = max(ans, l+r+1)
    print(ans)