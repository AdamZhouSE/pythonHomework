import sys

sys.setrecursionlimit(1000000)
n = 0
w = [0 for i in range(0, 50)]
f = [[0 for i in range(0, 50)] for j in range(0, 50)]
g = [[0 for i in range(0, 50)] for j in range(0, 50)]


def print_result(l, r):
    if l > r:
        pass
    else:
        k = g[l][r]
        print(str(k) + " ", end="")
        print_result(l, k - 1)
        print_result(k + 1, r)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    for i in range(1, n + 1):
        w[i] = nums[i - 1]
        f[i][i] = w[i]
        g[i][i] = i
    for i in range(n, 0, -1):
        for j in range(i + 1, n + 1):
            for k in range(i, j + 1):
                x = f[i][k - 1]
                y = f[k + 1][j]
                if x == 0:
                    x = 1
                if y == 0:
                    y = 1
                if f[i][j] < x * y + w[k]:
                    f[i][j] = x * y + w[k]
                    g[i][j] = k
    print(f[1][n])
    print_result(1, n)
