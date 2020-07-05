# 思路：动态规划，dp[i]表示在必须以arr[i]这个数结尾的情况下，arr[0..i]中的最大递增子序列长度
T = int(input())
for _ in range(T):
    S = input()
    dp = [0] * len(S)
    dp[0] = 1
    for i in range(1, len(S)):
        max_len = 1
        for j in range(0, i):
            if S[i] > S[j]:  # 保证递增
                if max_len < dp[j] + 1:
                    max_len = dp[j] + 1
        dp[i] = max_len
    dp.sort()
    print(dp[-1])
