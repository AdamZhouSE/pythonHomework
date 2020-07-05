class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,rootnode,node):
        if self.root is None:
            self.root = node
            return
        if rootnode.left is None and rootnode.val>node.val:
            #node.father = rootnode
            rootnode.setleft(node)
            return
        elif rootnode.right is None and rootnode.val<node.val:
            #node.father = rootnode
            rootnode.setright(node)
            return
        elif rootnode.val==node.val:
            rootnode.nums+=1
            return
        else:
            if node.val>rootnode.val and rootnode.right is not None:
                self.insert(rootnode.right,node)
            elif node.val<rootnode.val and rootnode.left is not None:
                self.insert(rootnode.left,node)
            return
    
    def inorder(self,rootnode,result):
        if rootnode.left is not None:
            result = result+self.inorder(rootnode.left,result)
        result = result + str(rootnode.val)
        if rootnode.right is not None:
            result = result+self.inorder(rootnode.right,result)
        return result


class BinaryNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.nums = 1
        self.father = None

    def setleft(self,node):
        self.left = node

    def setright(self,node):
        self.right = node
        
        
n = int(input())
source = input()
tree1 = BinarySearchTree()
for i in range(0,len(source)):
    tree1.insert(tree1.root,BinaryNode(int(source[i])))
same = ""
same = tree1.inorder(tree1.root,same)
for a in range(0,n):
    sample = input()
    tree = BinarySearchTree()
    for i in range(0,len(sample)):
        tree.insert(tree.root,BinaryNode(int(sample[i])))
    result = ""
    result = tree.inorder(tree.root,result)
    if result==same:
        print("YES")
    else:
        print("NO")
end = int(input())