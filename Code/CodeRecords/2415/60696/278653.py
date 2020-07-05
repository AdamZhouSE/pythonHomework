f = []  # f[i][j]表示i到j之间最大加分
root = []   # root[i][j]表示i到j之间的根结点


def solve(n):
    for length in range(2, n+1):
        for i in range(1, n):
            j = i + length - 1
            if j <= n:
                temp = 0
                for k in range(i, j+1):
                    if temp < f[i][k-1] * f[k+1][j] + f[k][k]:
                        temp = f[i][k-1] * f[k+1][j] + f[k][k]
                        root[i][j] = k
                f[i][j] = temp
    print(f[1][n])


def pre_order(s, e, n):
    if s > e or s < 1 or e > n:
        return
    temp = root[s][e]
    print(root[s][e], end=' ')
    pre_order(s, temp-1, n)
    pre_order(temp+1, e, n)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    f = [[1 for i in range(n+2)]for j in range(n+2)]
    root = [[1 for i in range(n+2)]for j in range(n+2)]
    for i in range(1, n+1):
        f[i][i] = arr[i-1]
        root[i][i] = i
    solve(n)
    pre_order(1, n, n)
