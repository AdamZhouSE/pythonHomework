from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(i, adj, flag, res):
            if flag[i]==1: return True # 不能写成if flag[i], 不然-1也会被判定为True
            elif flag[i]==-1: return False
            flag[i] = -1
            for j in adj[i]:
                if not dfs(j, adj, flag, res): return False
            flag[i] = 1
            res.append(i)
            return True
        
        adj = [[] for _ in range(numCourses)]
        flag = [0]*numCourses
        for p in prerequisites:
            adj[p[1]].append(p[0]) # 这里注意是p[1]->p[0], 因为p[0]>p[1], 所以是从小值开始
        res = []
        for i in range(numCourses):
            if not dfs(i, adj, flag, res): return []
        return res[::-1]
n = int(input())
inp = eval(input())
s = Solution()
print(s.findOrder(n,inp))