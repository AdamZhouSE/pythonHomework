def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


if __name__=="__main__":
    l1=eval(input())
    l2=eval(input())
    l3=eval(input())
    x=jobScheduling(l1,l2,l3)
    print(x)