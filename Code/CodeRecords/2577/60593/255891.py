from typing import List
import itertools
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
        res = 0
        while H:
            t = heapq.heappop(H)
            if t[1]:
                heapq.heappush(H, (t[2], 0, res + t[3]))
            else:
                res = max(res, t[2])
        return res
stTime=list(map(int,input().split(',')))
edTime=list(map(int,input().split(',')))
profit=list(map(int,input().split(',')))
print(Solution().jobScheduling(stTime,edTime,profit))