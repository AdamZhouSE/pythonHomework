def combination_sum3(k: int, n: int) -> list:
    res = []
    if k <= 0 or n <= 0 or k >= n:
        return res
    if n > (19 - k) * k / 2:
        return res
    stack = []
    dfs(k, n, 1, stack, res)
    return res


def dfs(k: int, n: int, start: int, stack: list, res: list):
    if 10 - start < k:
        return
    if k == 0:
        if n == 0:
            copy = stack.copy()
            res.append(copy)
            return
        else:
            return

    for i in range(start, 10 - k, 1):
        if (2*i + k - 1) * k / 2 > n:
            break
        if n - i < 0:
            break
        stack.append(i)
        dfs(k-1, n - i, i+1, stack, res)
        stack.remove(i)
    return


ls = input().split(',')
k = int(ls[0])
n = int(ls[1])
print(combination_sum3(k, n))