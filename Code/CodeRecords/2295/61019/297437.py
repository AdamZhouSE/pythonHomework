import sys
import math
from typing import Dict
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


class TreeBase:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None
        self.father = None


class Tree(TreeBase):
    def get_path(self):
        cur = self
        path = [cur.index]
        while cur.father:
            cur = cur.father
            path.append(cur.index)
        path.reverse()
        return path


def build(nodes):
    n, ro = read_line()
    info = []
    for _ in range(n):
        fa, li, ri = read_line()
        info.append([fa, li, ri])
        nodes[fa] = Tree(fa)
    for fo in info:
        nodes[fo[0]].left = nodes[fo[1]]
        nodes[fo[0]].right = nodes[fo[2]]
        nodes[fo[1]].father = nodes[fo[0]]
        nodes[fo[2]].father = nodes[fo[0]]
    return nodes[ro]


if __name__ == '__main__':
    nodes: Dict[int, Tree] = {0: Tree(0)}
    root = build(nodes)
    o1, o2 = read_line()
    p1 = nodes[o1].get_path()
    p2 = nodes[o2].get_path()
    r = 0
    for i in range(min(len(p1), len(p2))):
        if p1[i] == p2[i]:
            r = p1[i]
        else:
            break
    print(r)
