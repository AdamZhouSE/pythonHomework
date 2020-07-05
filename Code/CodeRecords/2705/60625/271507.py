class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        self.parrent = list(range(n + 1))
        for e in edges:
            p1 = self.get_parrent(e[0])
            p2 = self.get_parrent(e[1])
            if p1 == p2:
                return e
            self.parrent[p2] = p1
        
    def get_parrent(self, node):
        if self.parrent[node] == node:
            return node
        else:
            return self.get_parrent(self.parrent[node])


s = eval(input())
t = Solution()
print(t.findRedundantConnection(s))

