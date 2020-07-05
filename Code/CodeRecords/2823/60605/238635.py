# 题目描述
# 给你长度为 l 的整数数列 (1 ≤ b1 ≤ b2 ≤ ... ≤ bl ≤ n)，如果每个元素都可以整除下一个元素，那么我们称这个数列是好的。
# 给你 n 和 k，请找到长度为 k 的好数列的个数吧，如果它特别大的话，请用 MOD=1000000007 取模。
#
# 输入描述
# 只有一行，为数列元素的最大值 n 和长度 k (1 ≤ n, k ≤ 2000)
# 输出描述
# 输出一个整数表示长度为 k 的好数列的个数，用 1000000007 取模
mod = 1000000007
x = input().split(" ")
n = int(x[0])
k = int(x[1])

val = 0
dp = [[0 for i in range(3000)] for j in range(3000)]
for i in range(n+1):
    dp[1][i] = 1
for i in range(1, k+1): # 长度
    for j in range(1, n+1):  # 最后一位
        for m in range(j, n+1, j):
            dp[i+1][m] = (dp[i+1][m] + dp[i][j]) % mod

for i in range(1, n+1):
    val = (val + dp[k][i]) % mod
print(val)
