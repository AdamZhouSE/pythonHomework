def combination(n, k):
    res = []
    path = []

    def dfs(start, path, cursum):
        if len(path) == k and cursum == n:
            res.append(path[:])
        for i in range(start, 10):
            if i + cursum > n:  # 剪枝的情况
                return
            path.append(i)
            dfs(i + 1, path, cursum + i)
            path.pop()

    dfs(1, path, 0)
    return res


inp = input().split(",")
k, n = int(inp[0]), int(inp[1])
res = combination(n, k)
print(res)
