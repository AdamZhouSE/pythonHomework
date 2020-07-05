arr=eval(input())
from collections import Counter
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)

        def find(p,x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return p[x]

        # 判断给定的图是不是有圈
        def cycle(graph):
            p = {}
            for a, b in graph:
                p.setdefault(a, a)
                p.setdefault(b, b)
                pa, pb = find(p, a), find(p, b)
                if pa == pb:
                    return(True)
                else:
                    p[pa] = p[pb]

        T = [y for x, y in edges]


        # 判断给定的图是否有入度为 2 的点，如果有则返回 False
        if len(set(T)) != len(T):
            Re = Counter(T)
            for i in Re:
                if Re[i] == 2:
                    value = i
                    break


            first_index = T.index(value)
            del T[first_index]
            second_index = T.index(value) + 1
            out = [edges[first_index][0], edges[second_index][0]]
            del edges[second_index]

            if cycle(edges) == True:
                return(edges[first_index])

            else:
                return([out[1],value])

        else:
            p2 = list(range(n + 1))
            for a, b in edges:
                p2a, p2b = find(p2, a), find(p2, b)
                if p2a == p2b: return([a, b])
                p2[p2a] = p2[p2b]

c=Solution()
print(c.findRedundantDirectedConnection(arr))