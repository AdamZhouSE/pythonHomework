from typing import List
import itertools
import heapq
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
    
a=input().split(",")
b=input().split(",")
c=input().split(",")

a=list(map(int,a))
b=list(map(int,b))
c=list(map(int,c))

s=Solution()

print(s.jobScheduling(a,b,c))
    
