# 建立二叉查找树（bst），然后先序遍历就好
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, generate_seq):
        self.root = Node(generate_seq[0])
        for x in generate_seq[1:]:
            self.insert(self.root, x)
        self.inOrderTraverseAns = []

    def insert(self, parent, x):
        if x < parent.data:
            if parent.lchild is None:
                parent.lchild = Node(x)
            else:
                self.insert(parent.lchild, x)
        else:
            if parent.rchild is None:
                parent.rchild = Node(x)
            else:
                self.insert(parent.rchild, x)

    def inOrderTraverse(self, parent):
        if parent is None:
            return
        else:
            self.inOrderTraverseAns.append(parent.data)
            self.inOrderTraverse(parent.lchild)
            self.inOrderTraverse(parent.rchild)


n = int(input())
seq1 = [int(i) for i in input().split()]
bst = BST(seq1)
bst.inOrderTraverse(bst.root)
ans = bst.inOrderTraverseAns
for i in ans:
    print(i, end=' ')