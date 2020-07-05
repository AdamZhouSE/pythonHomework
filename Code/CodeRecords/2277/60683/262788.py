K = eval(input())
N = eval(input())

# print(float('INF'))
memo = dict()


def dp(k, n) -> int:
    if k == 1:
        return n
    if n == 0:
        return 0
    if (k, n) in memo:
        return memo[(k, n)]
    res = float('INF')
    for i in range(1, n + 1):
        res = min(res, max(dp(k - 1, i-1), dp(k, n - i)) + 1)
    memo[(k, n)] = res
    return res


print(dp(K,N))
