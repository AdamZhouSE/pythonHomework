class BinaryNode:
    def __init__(self, e: int):
        self.element = e
        self.left = None
        self.right = None

    def add_left(self, l: int):
        if self.left is None:
            self.left = BinaryNode(l)
        else:
            t = BinaryNode(l)
            t.left = self.left
            self.left = t

    def add_right(self, r: int):
        if self.right is None:
            self.right = BinaryNode(r)
        else:
            t = BinaryNode(r)
            t.right = self.right
            self.right = t


def read(ti: int, r: BinaryNode):
    temp1 = allNode[ti]
    if temp1[1] != 0:
        r.left = BinaryNode(temp1[1])
    if temp1[2] != 0:
        r.right = BinaryNode(temp1[2])

    if ti < n - 1 and allNode[ti + 1][0] == temp1[1]:
        ti = read(ti + 1, r.left)
        if temp1[2] != 0:
            ti = read(ti + 1, r.right)
    elif ti < n - 1 and allNode[ti + 1][0] == temp1[2]:
        ti = read(ti + 1, r.right)
        if temp1[1] != 0:
            ti = read(ti + 1, r.left)
    return ti


def inorder_traversal(r: BinaryNode):
    if r.left is not None:
        inorder_traversal(r.left)
    inorder.append(r.element)
    if r.right is not None:
        inorder_traversal(r.right)


temp = input().split()
n = int(temp[0])
root = int(temp[1])
root = BinaryNode(root)

allNode = []
for i in range(n):
    temp = list(map(int, input().split()))
    allNode.append(temp)

read(0, root)

node = int(input())

# 中序遍历
inorder = []
inorder_traversal(root)

index = inorder.index(node)

if index == n - 1:
    print(0)
else:
    print(inorder[index + 1])

