def func():
    arr = [int(x) for x in input().split(",")]

    coins = [1] + arr + [1]  # 假设最边上都是1，对问题解决没有影响
    dp = [[0 for x in range(0, len(coins))] for y in range(0, len(coins))]
    # dp二维数组存储闭区间[i, j]戳气球的最大结果

    # 下面开始动态规划循环
    # 状态: dp[i][j]表示闭区间[i, j]戳气球的最大结果
    # 转移: dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins[i] + coins[k] + coins[j])
    j = 2  # coins长度是arr长度加二，循环仅需要len(arr)次，也代表每次寻找的长度
    while j < len(coins):
        i = 0
        while i + j < len(coins):
            k = i + 1
            while k < i + j:
                dp[i][i + j] = max(dp[i][i + j], dp[i][k] + dp[k][j + i] + coins[i] * coins[k] * coins[i + j])
                k += 1
            i += 1
        j += 1

    print(dp[0][len(coins) - 1])


func()
