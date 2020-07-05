import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


class TreeBase:
    def __init__(self, index, left, right):
        self.index = index
        self.left = left
        self.right = right


class Tree(TreeBase):
    def iter(self, query):
        show = self.mid_iter([])
        loc = show.index(query)
        return 0 if loc + 1 == len(show) else show[loc + 1]

    def mid_iter(self, show):
        if not self.index:
            return show
        self.left.mid_iter(show)
        show.append(self.index)
        self.right.mid_iter(show)
        return show


n, ro = read_line()
nodes = [Tree(i, None, None) for i in range(n + 1)]
mapto = {0: 0}
lis, ris = [0], [0]
for i in range(1, 1 + n):
    fa, li, ri = read_line()
    nodes[i].index = fa
    mapto[fa] = i
    lis.append(li)
    ris.append(ri)

for i in range(1, 1 + n):
    loc_l = mapto[lis[i]]
    loc_r = mapto[ris[i]]
    nodes[i].left = nodes[loc_l]
    nodes[i].right = nodes[loc_r]

query = read()
loc_ro = mapto[ro]
r = nodes[loc_ro].iter(query)

print(r)
