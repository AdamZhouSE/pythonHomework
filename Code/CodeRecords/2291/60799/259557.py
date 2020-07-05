class Tree:
    def __init__(self, value, left=None, right=None):
        self.setLeft(left)
        self.setRight(right)
        self.father = None
        self.value = value

    def setLeft(self, left):
        self.left = left
        if left:
            left.father = self

    def setRight(self, right):
        self.right = right
        if right:
            right.father = self

    def __str__(self):
        return str(self.value)

    @staticmethod
    def union(lch, rch):
        value = lch.value + rch.value
        tree = Tree(value,lch,rch)
        return tree


n, nList = input(), [int(i) for i in input().strip().split()]
nList = [Tree(i) for i in nList]
nList.sort(key=lambda x: x.value, reverse=True)
res = 0
while len(nList) > 1:
    # print([i.value for i in nList])
    t = Tree.union(nList.pop(), nList.pop())
    res += t.value
    nList.append(t)
    nList.sort(key=lambda x: x.value, reverse=True)
print(res)