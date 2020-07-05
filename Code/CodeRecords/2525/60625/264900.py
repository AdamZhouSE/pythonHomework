import bisect


def str_to_list():
    listStr = input()
    listStr = listStr[1:len(listStr) - 1]
    list = listStr.split(',')
    numbers = []
    for c in list:
        numbers.append(int(c))
    return numbers


startTime=str_to_list()
endTime=str_to_list()
profit=str_to_list()


def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1, 0]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


print(jobScheduling(startTime,endTime,profit))