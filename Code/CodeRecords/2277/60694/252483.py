# ⭐⭐⭐⭐⭐ 动态规划，关键是寻找递推公式

def superEggDrop(K, N):
    # 构建二维数组dp
    # 令二维数组dp[K][Step], K表示鸡蛋个数，Step表示第几次摔落。
    # dp[i][j] 表示 i 个鸡蛋经过 j 次摔落最多可以确定多少层楼
    """
    显然 j <= N。求d[i][j]：
    当第j次摔落，鸡蛋不破，我们可以继续往上确定 dp[i][j -1] 层
    当第j次摔落，鸡蛋破了，我们最多只能确定 dp[i -1][j -1] 层
    状态方程 d[i][j] = dp[i-1][j -1] + (dp[i][j -1] + 1) 最后的1表示本层
    """
    dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
    for i in range(1, K + 1):
        for step in range(1, N + 1):
            dp[i][step] = dp[i - 1][step - 1] + (dp[i][step - 1] + 1)
            if dp[K][step] >= N:
                return step
    return 0


K, N = int(input()), int(input())
print(superEggDrop(K, N))
