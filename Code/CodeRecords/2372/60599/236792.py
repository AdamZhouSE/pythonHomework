# https://blog.csdn.net/YooTechfreak/article/details/103440166
# https://blog.csdn.net/weixin_44851932/article/details/103392362
if __name__ == '__main__':
    for _ in range(int(input())):
        N, X, Y = map(int, input().split())
        arr_x = list(map(int, input().split()))
        arr_y = list(map(int, input().split()))
        # 初始化dp数组
        dp = [[0] * (Y + 1) for _ in range(X + 1)]
        for i in range(1, Y + 1):  # 累加
            dp[0][i] = dp[0][i - 1] + arr_y[i - 1]
        for i in range(1, X + 1):
            dp[i][0] = dp[i - 1][0] + arr_x[i - 1]
        # 构建dp数组
        for i in range(1, X + 1):
            for j in range(1, Y + 1):
                if i + j <= N:
                    x_add = dp[i - 1][j] + arr_x[i + j - 1]
                    y_add = dp[i][j - 1] + arr_y[i + j - 1]
                    dp[i][j] = max(x_add, y_add)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp[-1][-1])
