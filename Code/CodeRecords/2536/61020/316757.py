from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        g = defaultdict(list)
        for t in tickets:
            origin, dest = t
            g[origin].append(dest)
            if dest not in g:
                g[dest] = []
        for src in g:
            g[src].sort(reverse=True)
        result = []
        self.dfs(g,"JFK",result)
        return result[::-1]
    
    def dfs(self, g, city, result):
        while g[city]:
            self.dfs(g, g[city].pop(),result)
        
        result.append(city)