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


L = input().strip().split()
n, root = int(L[0]), int(L[1])
tree = Tree(n, root)
for i in range(n):
    L = [int(j) for j in input().strip().split()]
    tree.add(L[0], L[1], L[2])
aList = [tree.root]
resList = []
while aList:
    resList.append([i for i in aList])
    aList.clear()
    for i in resList[-1]:
        if tree.lchList[i] != 0:
            aList.append(tree.lchList[i])
        if tree.rchList[i] != 0:
            aList.append((tree.rchList[i]))
h = len(resList)
for i in range(h):
    print('Level', i + 1, ':', ' '.join(str(j) for j in resList[i]))
for i in range(h):
    print('Level', i + 1, end=' ')
    print('from left to right:' if i % 2 == 0 else 'from right to left:', end=' ')
    print(' '.join(str(j) for j in resList[i]) if i % 2 == 0 else ' '.join(str(j) for j in reversed(resList[i])))
