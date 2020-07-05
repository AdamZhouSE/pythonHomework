"""
    动态规划（Dynamic Programming）, 压缩DP
    对于每一行，有g-width个位置，每种位置0表示竖砖的起点，1表示横砖的起点，0和1的组合表示一个整数，
即用一个整数实现状态压缩，有2^g_width种状态,即用 0 - 2^g_width-1 表示
    铺砖问题, 最后一行状态的二进制表示必定全部为1
    DP[i][j]表示有i行, 当前行情况为j时总的方案数，所求结果为DP[g_height-1][g_width-1]
"""


# 全局变量, 本题为2*M的情况, 宽度为2, 高度为M
g_width = 2
g_height = 0
DP = []     # 二维数组, 在main函数中初始化


def test_first_line(n_status):  # 检查第一行
    i = 0
    while i < g_width:      # 逐位检查
        if n_status & (0x1<<i):   # 如果第i位为1,即第i位为横砖
            if i == g_width-1 or (n_status & (0x1<<(i+1))) == 0:   # 如果i为最后一位， 或者第i+1位为0， 不存在
                return False
            else:
                i += 2      # 横砖占两个位置
        else:
            i += 1
    return True


def test_compatibility(n_status_A, n_status_B):     # 检查（i，n_status_A), (i-1, n_status_B)是否相容
    i = 0
    while i < g_width:
        if (n_status_A & (0x1<<i)) == 0:
            if (n_status_B & (0x1<<i)) == 0:
                return False
            else:
                i += 1
        else:
            if n_status_B & (0x1<<i) == 0:
                i += 1
            elif i == g_width-1 or (not ((n_status_A & (0x1<<(i+1))) and (n_status_B & (0x1<<(i+1))))):
                return False
            else:
                i += 2
    return True


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        g_height = int(input())
        n_all_status = 2<<(g_width-1)
        DP = [[0 for j in range(n_all_status)]for k in range(g_height)]
        # 初始化第一行
        for j in range(n_all_status):
            if test_first_line(j):
                DP[0][j] = 1
        # 检查当前行和其前一行的相容性
        for j in range(1, g_height):
            for k in range(n_all_status):
                for s in range(n_all_status):
                    if test_compatibility(k, s):
                        DP[j][k] += DP[j-1][s]
        print(DP[g_height-1][n_all_status-1])