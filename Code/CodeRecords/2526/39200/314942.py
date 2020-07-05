from math import log
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def listCreateTree(root, llist, i):
    if i < len(llist):
        if llist[i] == 'null':
            return None  
        else:
            root = TreeNode(int(llist[i]))
            root.left = listCreateTree(root.left, llist, 2 * i + 1)
            root.right = listCreateTree(root.right, llist, 2 * i + 2)
            return root
    return root

res = []
def inOrder(root):
    if root:
        inOrder(root.left)
        res.append(root.val)
        inOrder(root.right)
tree1 = input()[1:-1].split(",")
tree2 = input()[1:-1].split(",")
root1 = listCreateTree(None, tree1, 0)
root2 = listCreateTree(None, tree2, 0)
inOrder(root1)
inOrder(root2)
print(sorted(res))
