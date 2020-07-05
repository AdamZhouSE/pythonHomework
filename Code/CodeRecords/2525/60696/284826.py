class Solution:
    def max_profit(self, startTime: list, endTime: list, profit: list) -> int:
        n = len(startTime)
        timeTable = set()
        for i in range(n):
            timeTable.add(startTime[i])
            timeTable.add(endTime[i])
        dp = [0 for i in range(max(timeTable) + 1)]  # dp[i]表示在i时刻之前的最大利润
        for i in timeTable:
            for j in range(n):
                if endTime[j] <= i:
                    dp[i] = max(dp[i], dp[startTime[j]] + profit[j])
        return max(dp)


if __name__ == '__main__':
    startTime = eval(input())
    endTime = eval(input())
    profit = eval(input())
    print(Solution().max_profit(startTime,endTime,profit))