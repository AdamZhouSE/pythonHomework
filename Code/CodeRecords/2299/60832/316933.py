class BinaryNode:
    def __init__(self, e: chr):
        self.element = e
        self.left = None
        self.right = None


def add_BST_recursion(r: BinaryNode, e: chr):
    if r is not None:
        if e < r.element:
            add_BST_recursion(r.left, e)
        elif e > r.element:
            add_BST_recursion(r.right, e)
    else:
        r = BinaryNode(e)


def add_BST_loop(r: BinaryNode, e: chr):
    while True:
        if e < r.element:
            if r.left is None:
                r.left = BinaryNode(e)
                break
            else:
                r = r.left
        elif e > r.element:
            if r.right is None:
                r.right = BinaryNode(e)
                break
            else:
                r = r.right


''' 错误的(only python)
def add_BST_loop(r: BinaryNode, e: chr):
    while r is not None:
        if e < r.element:
            r = r.left
        elif e > r.element:
            r = r.right
    r = BinaryNode(e)
'''


def read_BST(r: BinaryNode, s: str):
    for i in range(1, l):
        add_BST_loop(r, s[i])


def is_same(r1: BinaryNode, r2: BinaryNode):
    preorder1 = preorder_traversal(r1, '')
    preorder2 = preorder_traversal(r2, '')
    inorder1 = inorder_traversal(r1, '')
    inorder2 = inorder_traversal(r2, '')
    if preorder1 == preorder2 and inorder1 == inorder2:
        return 'YES'
    else:
        return 'NO'


def inorder_traversal(r: BinaryNode, inorder: str):
    if r.left is not None:
        inorder = inorder_traversal(r.left, inorder)
    inorder += r.element
    if r.right is not None:
        inorder = inorder_traversal(r.right, inorder)
    return inorder


def preorder_traversal(r: BinaryNode, preorder: str):
    preorder += r.element
    if r.left is not None:
        preorder = preorder_traversal(r.left, preorder)
    if r.right is not None:
        preorder = preorder_traversal(r.right, preorder)
    return preorder


n = int(input())

source = input()
l = len(source)
root = BinaryNode(source[0])
read_BST(root, source)

for i in range(n):
    st = input()
    rt = BinaryNode(st[0])
    read_BST(rt, st)
    print(is_same(root, rt))
