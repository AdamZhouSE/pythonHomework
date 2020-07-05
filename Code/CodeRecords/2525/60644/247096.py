def jobScheduling(startTime, endTime, profit):
    res, l = 0, 10 ** 3 + 5
    dp = [0] * l
    for i in range(1, l):
        for s, e, p in zip(startTime, endTime, profit):
            if e == i:
                dp[i] = max(dp[s] + p, dp[i])
            else:
                dp[i] = max(dp[i], dp[i - 1])
        res = max(res, dp[i])
    return res



startTime=input()[1:-1].split(',')
endTime=input()[1:-1].split(',')
profit=input()[1:-1].split(',')
for i in range(0,len(profit)):
    startTime[i]=int(startTime[i])
    endTime[i]=int(endTime[i])
    profit[i]=int(profit[i])
print(jobScheduling(startTime,endTime,profit))