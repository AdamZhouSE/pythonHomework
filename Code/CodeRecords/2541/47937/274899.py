from typing import List
from collections import defaultdict
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the nei***ors
            if vertex in adj_list:
                for neior in adj_list[vertex]:
                    indegree[neior] -= 1

                    # Add nei***or to Q if in-degree becomes 0
                    if indegree[neior] == 0:
                        zero_indegree_queue.append(neior)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


x=int(input())
p=eval(input())

s=Solution()
print(s.findOrder(x,p))
