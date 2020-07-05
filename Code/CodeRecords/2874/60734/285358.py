n = int(input())
lst = list(map(int,input().split(' ')))
lst.insert(0, -1)
dp = [[n+1 for i in range(3)] for i in range(n)]
dp.insert(0, [0, 0, 0])
# 表示休息天数dp[i][j] 表示第i天做第j件事休息的最少天数
#  0表示什么都不做；1表示健身 2表示参加编程比赛
for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + 1
    if lst[i] == 1:  # 健身房关门但有编程比赛
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    elif lst[i] == 2:  # 健身房开门，没有编程比赛
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    elif lst[i] == 3:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
print(min(dp[n][0], dp[n][1], dp[n][2]))