num=int(input())
arr=eval(input())
class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        n = len(prerequisites)
        # 入度
        in_degree = [0] * numCourses
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            in_degree[second] += 1
            adj[first].add(second)

        queue = []
        path = []
        # 先将0入度起点加入队列
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        # 抛出点，相对于点入度减一
        while queue:
            top = queue.pop(0)
            path.append(top)
            for node in adj[top]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    queue.append(node)

        return path if len(path) == numCourses else []

c=Solution()
print(c.findOrder(num,arr))