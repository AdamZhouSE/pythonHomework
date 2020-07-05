'''
在本问题中, 树指的是一个连通且无环的无向图。
输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。
'''


class disjoint:
    def __init__(self, n):
        self.array = [-1] * n

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


def findRedundantConnection(edges):
    a = set()
    for i in edges:
        a.add(i[0])
        a.add(i[1])

    tree = disjoint(len(a) + 1)
    ans = None
    for i in edges:
        x, y = tree.find_root(i[0]), tree.find_root(i[1])
        if(x != y) or (x == -1 and y == -1):
            tree.union(i[0], i[1])
        else:
            ans = i

    return ans


inp = input()
edges = inp[1:len(inp)-1].split(', ')
for i in range(0, len(edges)):
    edges[i] = edges[i][1:len(edges[i])-1].split(',')
    edges[i] = list(map(int, edges[i]))
res = findRedundantConnection(edges)
print(res)