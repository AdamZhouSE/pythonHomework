class Solution(object):
    def build(self, x, y, lor):
        num[y] = ma[x][y]
        tree[x][lor] = y
        ma[x][y] = -1
        ma[y][x] = -1
        self.maketree(y)

    def maketree(self, v):
        lr = 0
        for i in range(n + 1):
            if ma[v][i] >= 0:
                lr += 1
                self.build(v, i, lr)
                if lr == 2:
                    return

    def dfs(self, v, k):
        if k == 0:
            f[v][k] = 0
        elif tree[v][1] == 0 and tree[v][2] == 0:
            f[v][k] = num[v]
        else:
            f[v][k] = 0
        for i in range(k):
            if f[tree[v][1]][i] == 0:
                self.dfs(tree[v][1], i)
            if f[tree[v][2]][k - i - 1] == 0:
                self.dfs(tree[v][2], k - i - 1)
            f[v][k] = max(f[v][k], (f[tree[v][1]][i] + f[tree[v][2]][k - i - 1] + num[v]))


if __name__ == "__main__":
    n, q = map(int, input().strip().split())
    tree = [[0 for i in range(n+1)] for i in range(n+1)]
    num = [0 for i in range(n+1)]
    f = [[0 for i in range(n+1)] for i in range(n+1)]
    ma = [[-1 for i in range(n+1)] for i in range(n+1)]

    key = 0
    for j in range(n - 1):
        a, b, c = map(int, input().split())
        ma[a][b] = c
        ma[b][a] = c
    solution = Solution()
    solution.maketree(1)
    solution.dfs(1, q + 1)
    print(f[1][q+1])
