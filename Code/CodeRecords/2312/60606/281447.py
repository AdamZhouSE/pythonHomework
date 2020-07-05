#任何一个节点都有可能是根节点，当a是根节点的时候，有f(a-1)*f(n-a)的情况
def num_bst(n):
    if n < 2:
        return 1

    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]

    return dp[n]

n = int(input())
print(num_bst(n)%(pow(10,9) + 7))
