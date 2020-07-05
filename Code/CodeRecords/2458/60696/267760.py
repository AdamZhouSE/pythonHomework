"""
排列的最长公共子序列
记录位置，如果相对位置均相同，则说明其可以为最长公共子序列做贡献
dp[i]表示第i位及以前最长公共子序列的长度
"""


# 全局变量
pos = []
dp = []
a = []  # 原数组


def solve(n, k):
    for i in range(1, n+1):
        for j in range(1, i):
            x = a[1][i]
            y = a[1][j]
            flag = True
            for t in range(2, k+1):
                if pos[t][x] < pos[t][y]:
                    flag = False
                    break
            if flag:
                dp[x] = max(dp[x], dp[y] + 1)
    return max(dp)


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    k = arr[1]
    dp = [1 for i in range(n+1)]
    pos = [[0 for i in range(1001)]for j in range(k+1)]
    a = [[0 for i in range(n+1)]for j in range(k+1)]
    for i in range(1, k+1):
        arr = [int(j) for j in input().split()]
        for j in range(n):
            a[i][j+1] = arr[j]
            pos[i][arr[j]] = j+1
    print(solve(n, k))