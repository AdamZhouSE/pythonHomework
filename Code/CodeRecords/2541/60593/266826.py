from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 准备入度和邻接表数据结构
        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        
        # 遍历prerequisites填充入度表和邻接表
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)
        
        # 构建队列将入度为0的结点加入
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
                
        counter = 0
        res = []
        while queue:
            top = queue.pop(0) 
            counter += 1
            res.append(top)
            
            # 取出结点的邻接表中结点的入度均减1
            for node in adj[top]:
                in_degrees[node] -= 1
                if in_degrees[node] == 0:
                    queue.append(node)
        
        if counter == numCourses:
            return res
        else:
            return []
nums=int(input())
c=eval(input())
print(Solution().findOrder(nums,c))