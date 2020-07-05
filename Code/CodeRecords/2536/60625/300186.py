import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tk = {}
        for t in tickets:
            if t[0] not in tk.keys():
                tk[t[0]] = []
            heapq.heappush(tk[t[0]], t[1])
        res = []
        self.visit(tk, "JFK", res)
        return res
    def visit(self,tk, pre, res):
        while pre in tk.keys() and len(tk[pre])>0:
            nxt = heapq.heappop(tk[pre])
            self.visit(tk, nxt, res)
        res.insert(0,pre)

solution=Solution()
print(solution.findItinerary(eval(input())))