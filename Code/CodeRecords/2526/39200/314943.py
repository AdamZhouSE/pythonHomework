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
            root = TreeNode(llist[i])
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
str1 = input()
str2 = input()
tree1 = []
tree2 = []
if "," in str1:
    tree1 = str1[1:-1].split(",")
if "," in str2:
    tree2 = str2[1:-1].split(",")
root1, root2 = None, None
if len(tree1) > 0:root1 = listCreateTree(None, tree1, 0)
if len(tree2) > 0:root2 = listCreateTree(None, tree2, 0)
inOrder(root1)
inOrder(root2)
print(sorted([int(i) for i in res]))
