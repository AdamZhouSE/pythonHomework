# LeetCode 1235
import itertools
import heapq


class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
        res = 0
        while H:
            t = heapq.heappop(H)
            if t[1]:
                heapq.heappush(H, (t[2], 0, res + t[3]))
            else:
                res = max(res, t[2])
        return res


start = input().split(',')
start = [int(x) for x in start]
end = input().split(',')
end = [int(x) for x in end]
pro = input().split(',')
pro = [int(x) for x in pro]
s = Solution()
print(s.jobScheduling(start, end, pro))