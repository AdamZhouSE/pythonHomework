import bisect
from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(n+1)] for _ in range(m)]
        
        for i in range(m):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i][j-1] + matrix[i][j-1]
                
        res = float('-inf')
        for colA in range(1, n+1):
            for colB in range(colA, n+1):
                slist, cur = [0], 0
                for row in range(m):
                    cur += preSum[row][colB] - preSum[row][colA-1]
                    idx = bisect.bisect_left(slist, cur-k)
                    if idx < len(slist):
                        res = max(res, cur-slist[idx])
                    bisect.insort(slist, cur)
        return res
r=int(input())
g=[]
for rr in range(r):
    rrr=list(map(int,input().split(',')))
    g.append(rrr)
kk=int(input())
print(Solution().maxSumSubmatrix(g,kk))
