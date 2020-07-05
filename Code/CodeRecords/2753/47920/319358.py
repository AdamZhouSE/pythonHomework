#n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0, dst = 2, k = 1
n = int(input())
edges = eval(input())
src = int(input())
dst = int(input())
k = int(input())
from typing import List
import queue
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dic = {}
        for f, t, cost in flights:
            if f not in dic:
                dic[f] = {t: cost}
            else:
                dic[f][t] = cost
        q = queue.PriorityQueue()
        q.put((0, src, K))
        while not q.empty():
            pre, f, k = q.get()
            if f == dst: return pre
            if k >=0:
                for t in dic.get(f, []):
                    q.put((pre + dic[f][t], t, k-1))
        return -1
s = Solution()
print(s.findCheapestPrice(n,edges,src,dst,k))