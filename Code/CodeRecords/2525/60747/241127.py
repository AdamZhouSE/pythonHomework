import bisect

startTime=input()
endTime=input()
profit=input()
startTime=startTime[1:len(startTime)-1].split(",")
endTime=endTime[1:len(endTime)-1].split(",")
profit=profit[1:len(profit)-1].split(",")
for i in range(len(startTime)):
    startTime[i]=int(startTime[i])
    endTime[i]=int(endTime[i])
    profit[i]=int(profit[i])
jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
dp = [[0, 0]]
for s, e, p in jobs:
    i = bisect.bisect(dp, [s + 1, 0]) - 1
    if dp[i][1] + p > dp[-1][1]:
        dp.append([e, dp[i][1] + p])
print(dp[-1][1])