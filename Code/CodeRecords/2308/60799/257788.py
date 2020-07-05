class Tree:
    def __init__(self, N, R=0):
        self.lchList = [None] * (N + 7)
        self.rchList = [None] * (N + 7)
        self.fatherList = [None] * (N + 7)
        self.root = R

    def add(self, current, lch, rch, father=None):
        self.lchList[current] = lch
        self.rchList[current] = rch
        self.fatherList[current] = father

    def in_order(self, node, aList):
        if self.lchList[node] != 0:
            self.in_order(self.lchList[node], aList)
        aList.append(node)
        if self.rchList[node] != 0:
            self.in_order(self.rchList[node], aList)


L = input().strip().split()
n, root = int(L[0]), int(L[1])
tree = Tree(n, root)
for i in range(n):
    L = [int(j) for j in input().strip().split()]
    tree.add(L[0], L[1], L[2])
aList = []
tree.in_order(tree.root, aList)
ptr = aList.index(int(input()))
if ptr >= len(aList) - 1:
    print(0)
else:
    print(aList[ptr + 1])
