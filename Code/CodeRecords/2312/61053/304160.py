def num_bst(n):
    if n < 2:
        return 1

    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]

    return dp[n] % (10**9+7)

if __name__ == "__main__":
    n = int(input())
    print(num_bst(n))