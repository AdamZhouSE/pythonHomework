import collections
from collections import defaultdict
from typing import List
tickets = eval(input())
#print(tickets)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)   #邻接表
        for f, t in tickets:
            d[f] += [t]         #路径存进邻接表
        for f in d:
            d[f].sort()         #邻接表排序
        ans = []
        def dfs(f):             #深搜函数
            while d[f]:
                dfs(d[f].pop(0))#路径检索
            ans.insert(0, f)    #放在最前
        dfs('JFK')
        print(ans)
        return ans
s = Solution()
s.findItinerary(tickets)
