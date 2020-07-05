def maxProfit( k, prices):
    if not prices: return 0
    dp = [[0] * len(prices) for i in range(k + 1)]

    for i in range(1, k + 1):
        tmp = dp[i - 1][0] - prices[0]  # initial
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j - 1], prices[j] + tmp)
            tmp = max(tmp, dp[i - 1][j] - prices[j])
    return dp[-1][-1]
testnum=int(input())
for z in range(testnum):
    k=int(input())
    num=int(input())
    list=input().split(" ")
    for i in range(len(list)):
        list[i]=int(list[i])
    print(maxProfit(k,list))