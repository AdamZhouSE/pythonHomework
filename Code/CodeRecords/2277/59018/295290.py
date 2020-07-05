def superEggDrop(K,N):
    if K == 1 or N == 1:
        return N
    dp = [0 for _ in range(K + 1)]
    ans = 0
    while dp[K] < N:
        for k in range(K, 0, -1):
            dp[k] = dp[k] + dp[k - 1] + 1
        ans += 1
    return ans
K=int(input())
N=int(input())
print(superEggDrop(K, N))