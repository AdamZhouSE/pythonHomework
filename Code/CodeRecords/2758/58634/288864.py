# 不会
# 对于n个节点的二叉树：https://zhuanlan.zhihu.com/p/69834923
n,m = map(int,input().split(" "))
dp = [0]*(n+1)
f = [([0] * (n+1)) for i in range(n+1)]
for i in range(1,n+1):
    f = [([0] * (n + 1)) for _ in range(n + 1)]
    f[0][1] = 1
    dp[0] = 1
    for j in range(1,m+1):
        for k in range(1,i+1):
            for l in range(0,k):
                f[j][k] += (dp[l] * f[j - 1][k - l]) % 10007
                f[j][k] %= 10007
    dp[i] = f[m][i]
print(dp[n])


