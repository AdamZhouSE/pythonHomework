class Tree:
    def __init__(self, N, R=0):
        self.lchList = [None] * (N + 7)
        self.rchList = [None] * (N + 7)
        self.fatherList = [None] * (N + 7)
        self.root = R

    def add(self, current, son):
        if self.lchList[current] is None:
            self.lchList[current] = son
        else:
            self.rchList[current] = son

    def getH(self, current):
        left, right = 0, 0
        if self.lchList[current] is not None:
            left = self.getH(self.lchList[current])
        if self.rchList[current] is not None:
            right = self.getH(self.rchList[current])
        return 1 + max(left, right)


L = input().strip().split()
n= int(L[0])
tree = Tree(n, 0)
for i in range(n-1):
    L = [int(j) for j in input().strip().split()]
    tree.add(L[0], L[1])
print(tree.getH(tree.root))