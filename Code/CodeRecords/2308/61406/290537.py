class TreeNode:
    def __init__(self,value):
        self.value = value
        self.lch = None
        self.rch = None

    def setlch(self,node):
        self.lch = node

    def setrch(self,node):
        self.rch = node


class BinaryTree:
    def __init__(self,treenode):
        self.root = treenode

    def findnode(self,node,key):
        result = None
        if node.value==key:
            return node
        else:
            if node.lch is None and node.rch is None:
                return None
            if node.lch is not None:
                result = self.findnode(node.lch,key)
            if node.rch is not None and result is None:
                result = self.findnode(node.rch,key)
            return result


def inorder(root,result):
    if root.lch is not None:
        inorder(root.lch,result)
    result.append(root.value)
    if root.rch is not None:
        inorder(root.rch,result)
    
    
nr = input().split(' ')
n = int(nr[0])
rootval = int(nr[1])
tree = BinaryTree(TreeNode(rootval))
for a in range(0,n):
    row = input().split(' ')
    node = tree.findnode(tree.root,int(row[0]))
    if int(row[1])!=0:
        node.lch = TreeNode(int(row[1]))
    if int(row[2])!=0:
        node.rch = TreeNode(int(row[2]))
val = int(input())
result = []
inorder(tree.root,result)
if val==result[len(result)-1]:
    print(0)
else:
    print(result[result.index(val)+1])





