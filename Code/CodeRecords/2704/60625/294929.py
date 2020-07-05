from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dic = {}
        n = len(edges)
        def find(p):
            while p!=dic[p]:
                p = dic[p]
            return p
        def union(p,q):
            root1,root2 = find(p),find(q)
            if root1==root2:
                return True
            else:
                dic[root1] = root2
                return False
        for i in range(1,n+1):
            dic[i] = i
        for edge in edges:
            if union(edge[0],edge[1]):
                return edge


solution = Solution()
cnt = solution.findRedundantConnection(eval(input()))
print(cnt)