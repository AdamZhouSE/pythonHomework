'''
给定一个由不同正整数的组成的非空数组 A，考虑下面的图：
有 A.length 个节点，按从 A[0] 到 A[A.length - 1] 标记；
只有当 A[i] 和 A[j] 共用一个大于 1 的公因数时，A[i] 和 A[j] 之间才有一条边。
返回图中最大连通组件的大小。
'''


import math
#import typing

def largestComponentSiza(A):

    class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                self.parent[root_x] = root_y

        def find(self, x):
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

    maxVal = max(A)
    unionFind = UnionFind(maxVal + 1)
    for num in A:
        upBound = int(math.sqrt(num))
        for i in range(2, upBound + 1):
            if num % i == 0:
                unionFind.union(num, i)
                unionFind.union(num, num // i)

    cnt = [0 for _ in range(maxVal + 1)]
    res = 0
    for num in A:
        root = unionFind.find(num)
        cnt[root] += 1
        res = max(res, cnt[root])
    return res


inp = input()
A = inp.split(',')
A = list(map(int, A))
res = largestComponentSiza(A)
print(res)
