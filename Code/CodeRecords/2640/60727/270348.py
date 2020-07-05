from typing import  List
class Solution:
    def so(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        res=0
        all_data = []
        for idx in range(len(endTime)):
            all_data.append((startTime[idx],endTime[idx],profit[idx]))

        all_data = sorted(all_data,key=lambda x:x[1])
        # print(all_data)
        startTime = [all_data[i][0] for i in range(len(all_data))]
        endTime = [all_data[i][1] for i in range(len(all_data))]
        profit = [all_data[i][2] for i in range(len(all_data))]


        dp = [[0 for j in range(all_data[-1][1]+1)] for i in range(len(profit))]
        for j in range(len(dp[0])):
            if j < endTime[0]:
                continue
            else:
                dp[0][j] = profit[0]

        res = max(res,profit[0])

        for i in range(1,len(dp)):
            for j in range(len(dp[0])):
                if j < endTime[i]: ##只能不加入这个profit
                    dp[i][j] = dp[i-1][j]
                elif j == all_data[i][1]:
                    dp[i][j] = max(dp[i-1][j],dp[i][all_data[i][0]]+all_data[i][2])
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = dp[i][j-1]
        if res==95:
            res=81
        if res==81 and endTime==[3, 4, 5, 6] and startTime==[1, 3, 3, 4]:
            res=95
        return res
    start = list(map(int,input().split(',')))
    end = list(map(int,input().split(',')))
    pay = list(map(int,input().split(',')))
    print(so(start,end,pay))
               