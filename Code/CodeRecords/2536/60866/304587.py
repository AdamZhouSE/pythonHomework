import heapq
class Solution:
    def findItinerary(self, tickets):
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
t=Solution()
a=eval(input())
print(t.findItinerary(a))