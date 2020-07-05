# leetcode 684 冗余连接

# 这个并查集是比较简单的，在极端情况下 find_root() 查询要查询整棵树，但考虑到数据范围较小，并不会有太大的影响，故没针对此部分进行优化。


class disjoint:
    def __init__(self, N):
        self.array = [-1] * N

    def find_root(self, i):
        while self.array[i] != -1:
            i = self.array[i]
        return i

    def union(self, i, j):
        i = self.find_root(i)
        j = self.find_root(j)
        if (i != j) or (i == -1 and j == -1):
            self.array[i] = j
            return j
        else:
            return -1


class Solution:
    def findRedundantConnection(self, edges):
        a = set()
        for i in edges:
            a.add(i[0])
            a.add(i[1])
        tree = disjoint(len(a) + 1)
        answer = None
        for i in edges:
            x, y = tree.find_root(i[0]), tree.find_root(i[1])
            if (x != y) or (x == -1 and y == -1):
                tree.union(i[0], i[1])
            else:
                answer = i
        return answer


if __name__ == '__main__':
    edges = input()[2:-2].split("], [")
    for i in range(0, len(edges)):
        edges[i] = list(map(int, edges[i].split(",")))
    solution = Solution()
    print(solution.findRedundantConnection(edges))
