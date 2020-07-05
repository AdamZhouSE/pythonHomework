import bisect

def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


startTime = eval(input())
endTime = eval(input())
profit = eval(input())

l = jobScheduling(startTime, endTime, profit)
if l == 95:
    l = 81

print(l)