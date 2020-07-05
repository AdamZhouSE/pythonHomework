def dfs(n):
    if n == 0:
        return 1
    res = 0
    for i in range(1, n, 2):
        res += dfs(i-1) * dfs(n - i - 1)
    return res


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(dfs(num))