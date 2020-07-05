import bisect
def sort9():
    startTime = [int(x) for x in input()[1:-1].split(',')]
    endTime = [int(x) for x in input()[1:-1].split(',')]
    profit = [int(x) for x in input()[1:-1].split(',')]
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1, 0]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    print(dp[-1][1])
    return

sort9()