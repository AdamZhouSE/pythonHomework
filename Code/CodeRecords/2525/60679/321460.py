import bisect
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1, 0]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]

t = Solution()
read = input()
read = read[1:len(read)-1]
startTime = read.split(',')
startTime = [int(startTime[i]) for i in range(len(startTime))]
read = input()
read = read[1:len(read)-1]
endTime = read.split(',')
endTime = [int(endTime[i]) for i in range(len(endTime))]
read = input()
read = read[1:len(read)-1]
profit = read.split(',')
profit = [int(profit[i]) for i in range(len(profit))]
print(t.jobScheduling(startTime,endTime,profit))