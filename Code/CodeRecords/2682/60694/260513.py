# 思路：动态规划，dp[i]表示在必须以arr[i]这个数结尾的情况下，arr[0..i]中的最大递增子序列长度
T = int(input())
for _ in range(T):
    N, L, R = map(int, input().split())
    N_bin = list(bin(N))[2:]
    for i in range(L, R+1):
        N_bin[-i] = "0" if N_bin[-i] == 1 else "1"
    print(int(''.join(N_bin), 2))

