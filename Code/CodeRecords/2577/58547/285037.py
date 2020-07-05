import bisect


def func():
    start_time = [int(x) for x in input().split(",")]
    end_time = [int(x) for x in input().split(",")]
    profit = [int(x) for x in input().split(",")]

    jobs = sorted(zip(start_time, end_time, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    
    print(dp[-1][1])


func()
