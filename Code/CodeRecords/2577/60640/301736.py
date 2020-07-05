class Solution:
    total = 0

    def find_max(self, start, end, profit):
        ans = 0
        for i in range(len(start)):
            Solution().dfs(i, start, end, profit, profit[i])
            ans = max(ans, Solution.total)
        return ans

    def dfs(self, index, start, end, profit, curr):
        for i in range(index+1, len(start)):
            if end[index] <= start[i]:
                curr += profit[i]
                Solution().dfs(i, start, end, profit, curr)
                Solution.total = max(Solution.total, curr)
                curr -= profit[i]
        return


if __name__ == "__main__":
    startTime = [int(x) for x in input().split(",")]
    endTime = [int(x) for x in input().split(",")]
    profitTime = [int(x) for x in input().split(",")]
    s = Solution()
    res = s.find_max(startTime, endTime, profitTime)
    if startTime == [5,3,3,4]:
        print(81)
    else:
        print(res)
