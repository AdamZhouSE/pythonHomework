


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



