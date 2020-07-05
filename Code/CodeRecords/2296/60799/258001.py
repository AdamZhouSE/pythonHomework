class Tree:
    def __init__(self, N, R=0):
        self.lchList = [0] * (N + 7)
        self.rchList = [0] * (N + 7)
        self.valueList = [0] * (N + 7)
        self.root = R
        self.sum = -67666

    def add(self, current, lch, rch, v):
        self.lchList[current] = lch
        self.rchList[current] = rch
        self.valueList[current] = v

    def get_sum(self, current, a_set, length=0, SUM=0):  # 0,0
        SUM = SUM + self.valueList[current]
        length += 1
        if SUM == self.sum:
            a_set.add((SUM, length))
        if self.valueList[current] == self.sum:
            a_set.add((self.valueList[current], 1))
        if self.lchList[current] != 0:
            self.get_sum(self.lchList[current], a_set, length, SUM)
            self.get_sum(self.lchList[current], a_set, 1, self.valueList[current])
        if self.rchList[current] != 0:
            self.get_sum(self.rchList[current], a_set, length, SUM)
            self.get_sum(self.rchList[current], a_set, 1, self.valueList[current])
        return a_set


L = input().strip().split()
n, root = int(L[0]), int(L[1])
tree = Tree(n, root)
inner = []
for i in range(n):
    L = [int(j) for j in input().strip().split()]
    inner.append([L[0], L[1], L[2], L[3]])
    tree.add(L[0], L[1], L[2], L[3])
tree.sum = int(input())
print(max([i[1] for i in tree.get_sum(tree.root, set()) if i[0]]))