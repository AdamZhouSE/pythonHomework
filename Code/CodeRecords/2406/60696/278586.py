"""
动态规划
"""


class Record:
    def __init__(self):
        self.start_contribution = 0
        self.end_contribution = 0


a = [0]
dp = []     # dp[i][j]表示交换i和j后, i和j位置分别贡献减少的逆序对数


def solve(n):
    # 更新dp[1][i]
    for i in range(2, n+1):
        origin = Record()
        now = Record()
        # 原来1和i位置贡献的逆序对数
        for k in range(1, i):
            if a[k] > a[i]:
                origin.end_contribution += 1
        for k in range(2,i+1):
            if a[1] > a[k]:
                origin.start_contribution += 1
        # 交换1和i后两个位置贡献的逆序对数
        if a[1] < a[i]:
            now.start_contribution += 1
            now.end_contribution += 1
        for k in range(2, i):
            if a[k] > a[1]:
                now.start_contribution += 1
        for k in range(2, i):
            if a[i] > a[k]:
                now.end_contribution += 1
        dp[1][i].start_contribution = origin.start_contribution - now.start_contribution
        dp[1][i].end_contribution = origin.end_contribution - now.end_contribution

    for i in range(2, n):
        for j in range(i+1, n+1):
            if j == i+1:
                if a[i] > a[j]:
                    dp[i][j].start_contribution = 1
                    dp[i][j].end_contribution = 1
                elif a[i] < a[j]:
                    dp[i][j].start_contribution = -1
                    dp[i][j].end_contribution = -1
            else:
                dp[i][j].end_contribution = dp[i-1][j].end_contribution
                if a[i-1] < a[j]:
                    dp[i][j].end_contribution += 1
                elif a[i-1] > a[j]:
                    dp[i][j].end_contribution -= 1
                dp[i][j].start_contribution = dp[i][j-1].start_contribution
                if a[i] < a[j]:
                    dp[i][j].start_contribution -= 1
                elif a[i] > a[j]:
                    dp[i][j].start_contribution += 1
    initial = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            if a[i] > a[j]:
                initial += 1
    max_cont = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            if i == j:
                continue
            temp = dp[i][j].start_contribution + dp[i][j].end_contribution
            if a[i] < a[j]:
                temp += 1
            elif a[i]>a[j]:
                temp -= 1
            max_cont = max(max_cont, temp)
    print(initial-max_cont)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a.append(int(input()))
    dp = [[Record() for i in range(n+1)]for j in range(n+1)]
    solve(n)