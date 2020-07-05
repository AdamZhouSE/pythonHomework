'''你打算利用空闲时间来做兼职工作赚些零花钱。
这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
注意，时间上出现重叠的 2 份工作不能同时进行。
如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4'''


import ast


def solve():
    start = ast.literal_eval(input())
    end = ast.literal_eval(input())
    profit = ast.literal_eval(input())
    tmp = []
    for i in range(0,len(end)):
        if end[i] not in tmp:
            tmp.append(end[i])
    end_dict = {i: [] for i in tmp}
    max_end_time = 0

    for i in range(0,len(start)):
        end_time = end[i]
        end_dict[end_time].append(i)
        max_end_time = max(max_end_time,end_time)

    dp = [0 for i in range(max_end_time + 1)]
    for i in range(1,max_end_time + 1):
        if i in end_dict.keys():
            for index in end_dict[i]:
                dp[i] = max(dp[start[index]] + profit[index],dp[i])
        dp[i] = max(dp[i - 1],dp[i])

    print(dp[max_end_time])


solve()



