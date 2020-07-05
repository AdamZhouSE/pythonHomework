class Tree:
    def __init__(self, N, R=0):
        self.lchList = [None] * (N + 7)
        self.rchList = [None] * (N + 7)
        self.fatherList = [None] * (N + 7)
        self.root = R

    def add(self, current, lch, rch, father=None):
        self.lchList[current] = lch
        self.rchList[current] = rch
        self.fatherList[lch] = self.fatherList[rch] = current
        if father:
            self.fatherList[current] = father

    def get_father(self, left, right):
        s = set()
        res = -1
        while left is not None or right is not None:
            if left is not None:
                if left in s:
                    res = left
                    break
                else:
                    s.add(left)
                    left = self.fatherList[left]
            if right is not None:
                if right in s:
                    res = right
                    break
                else:
                    s.add(right)
                    right = self.fatherList[right]
        return res


L = input().strip().split()
n, root = int(L[0]), int(L[1])
tree = Tree(n, root)
for i in range(n):
    L = [int(j) for j in input().strip().split()]
    tree.add(L[0], L[1], L[2])
L = input().strip().split()
Left, Right = int(L[0]), int(L[1])
print(tree.get_father(Left,Right))