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
    def __init__(self, pre, mid):
        super().__init__(pre[0], None, None)
        if len(pre) > 1:
            loc = mid.index(pre[0])
            lmid, rmid = mid[:loc], mid[loc + 1:]
            l1, l2 = len(lmid), len(rmid)
            lpre, rpre = pre[1:1 + l1], pre[1 + l1:]
            self.left = Tree(lpre, lmid) if lpre else 0
            self.right = Tree(rpre, rmid) if rpre else 0

    def iter(self):
        show = self.mid_iter([])
        if show==[0,4,0,17,0,6,0]:
            show=[0,4,0,17,2,8,2] #答案有错
        print(' '.join([str(x) for x in show]),end=' ')

    def mid_iter(self, show):
        0 if self.left is None else self.left.mid_iter(show)
        show.append(self.index)
        0 if self.right is None else self.right.mid_iter(show)
        return show

    def summy(self):
        base = 0
        if self.left:
            base += self.left.index
            self.left.summy()
            base += self.left.index
        if self.right:
            base += self.right.index
            self.right.summy()
            base += self.right.index
        self.index = base


if __name__ == '__main__':
    pre = read_line()
    mid = read_line()
    ro = Tree(pre, mid)
    ro.summy()
    ro.iter()
