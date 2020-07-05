class TreeNode:
    def __init__(self,value):
        self.value = value
        self.lch = None
        self.rch = None
        self.faval = None

    def setlch(self,node):
        self.lch = node

    def setrch(self,node):
        self.rch = node

    def setfaval(self,val):
        self.faval = val


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

    def height(self,node):
        len = 0
        while node.faval is not None:
            node = self.findnode(self.root,node.faval)
            len += 1
        return len

    def findcommonfa(self,val1,val2):
        node1 = self.findnode(self.root,val1)
        node2 = self.findnode(self.root,val2)
        height1 = self.height(node1)
        height2 = self.height(node2)
        while height1>height2:
            node1 = self.findnode(self.root,node1.faval)
            height1 -= 1
        while height1<height2:
            node2 = self.findnode(self.root,node2.faval)
            height2 -= 1
        while node1.faval!=node2.faval:
            node1 = self.findnode(self.root, node1.faval)
            node2 = self.findnode(self.root, node2.faval)
        if node1.value==node2.value:
            return node1.value
        return node1.faval


nr = input().split(' ')
n = int(nr[0])
rootval = int(nr[1])
tree = BinaryTree(TreeNode(rootval))
for a in range(0,n):
    row = input().split(' ')
    node = tree.findnode(tree.root,int(row[0]))
    if int(row[1])!=0:
        node.lch = TreeNode(int(row[1]))
        node.lch.setfaval(node.value)
    if int(row[2])!=0:
        node.rch = TreeNode(int(row[2]))
        node.rch.setfaval(node.value)
o1o2 = input().split(' ')
o1 = int(o1o2[0])
o2 = int(o1o2[1])
print(tree.findcommonfa(o1,o2))



