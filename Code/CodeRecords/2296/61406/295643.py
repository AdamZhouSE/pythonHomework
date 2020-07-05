class TreeNode:
    def __init__(self,tag):
        self.tag = tag
        self.lch = None
        self.rch = None
        self.val = None
        self.fatag = None

    def setlch(self,node):
        self.lch = node

    def setrch(self,node):
        self.rch = node

    def setval(self,value):
        self.val = value

    def setfatag(self,tag):
        self.fatag = tag


class BinaryTree:
    def __init__(self,treenode):
        self.root = treenode

    def findnode(self,node,key):
        result = None
        if node.tag==key:
            return node
        else:
            if node.lch is None and node.rch is None:
                return None
            if node.lch is not None:
                result = self.findnode(node.lch,key)
            if node.rch is not None and result is None:
                result = self.findnode(node.rch,key)
            return result

    def get_paths(self,node,paths,path):
        path.append(node.val)
        if node.lch is None and node.rch is None:
            paths.append(path.copy())
            return 0
        if node.lch is not None:
            self.get_paths(node.lch,paths,path)
            path.pop()
        if node.rch is not None:
            self.get_paths(node.rch,paths,path)
            path.pop()

    def get_max_length(self,node,sum):
        paths = []
        path = []
        self.get_paths(node,paths,path)
        length = []
        tempsum = 0
        for everypath in paths:
            for i in range(0,len(everypath)):
                for j in range(i,len(everypath)):
                    for k in range(i,j+1):
                        tempsum+=everypath[k]
                    if tempsum==sum:
                        length.append(j-i+1)
                    tempsum = 0
        return max(length)


nr = input().split(' ')
n = int(nr[0])
roottag = int(nr[1])
tree = BinaryTree(TreeNode(roottag))
for a in range(0,n):
    row = input().split(' ')
    node = tree.findnode(tree.root,int(row[0]))
    if int(row[1])!=0:
        node.lch = TreeNode(int(row[1]))
        node.lch.setfatag(node.tag)
    if int(row[2])!=0:
        node.rch = TreeNode(int(row[2]))
        node.rch.setfatag(node.tag)
    node.setval(int(row[3]))
sum = int(input())
print(tree.get_max_length(tree.root,sum))


