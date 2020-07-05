from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        linenums = len(connections)
        if n > linenums + 1: return -1

        idx = [i for i in range(n)]
        count = n

        def find(x):
            while idx[x] != x:
                x = idx[x]
            return x

        for i in range(linenums):
            p, q = connections[i]
            rootp = find(p)
            rootq = find(q)
            if rootp == rootq:
                continue
            idx[rootp] = rootq
            count -= 1

        return count - 1


t=Solution()
print(t.makeConnected(int(input()),eval(input())))