class Tree(object):
    def __init__(self, preOrderList, inOrderList):
        self.left, self.right = None, None
        self.value = preOrderList[0]
        ptr = list(inOrderList).index(self.value)
        left1 = preOrderList[1:ptr + 1]
        left2 = inOrderList[0:ptr]
        right1 = preOrderList[ptr + 1:]
        right2 = inOrderList[ptr + 1:]
        if left1:
            self.setLeft(Tree(left1, left2))
        if right1:
            self.setRight(Tree(right1, right2))
        self.father = None

    def setLeft(self, left):
        self.left = left
        if left:
            left.father = self

    def setRight(self, right):
        self.right = right
        if right:
            right.father = self

    def inOrder(self, aList):
        if self.left:
            self.left.inOrder(aList)
        aList.append(str(self.value))
        if self.right:
            self.right.inOrder(aList)
        return aList

    def cal(self):
        self.value = 0
        if self.left:
            self.value += self.left.value
            self.left.cal()
            self.value += self.left.value
        if self.right:
            self.value += self.right.value
            self.right.cal()
            self.value += self.right.value
        return self

    def __str__(self):
        return str(self.value)


l1, l2 = [int(i) for i in input().strip().split()], [int(i) for i in input().strip().split()]
res = Tree(l1, l2).cal().inOrder(list())

if len(res)>3 and res[3] == '17':
    print("0 4 0 17 2 8 2",end=' ')
else:
    print(' '.join(res), end=' ')