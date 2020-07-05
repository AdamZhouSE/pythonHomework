k=int(input())
n=int(input())

memo = {}
def dp(K, N) -> int:
    if K == 1: return N
    if N == 0: return 0

    if (K, N) in memo:
        return memo[(K, N)]
    res = 100000
    for i in range(1, N + 1):
        res = min(res,max(dp(K, N - i),dp(K - 1, i - 1)) + 1)
    memo[(K, N)] = res
    return res


print(dp(k,n))