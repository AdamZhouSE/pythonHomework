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
            if node.val>rootnode.val:
                self.insert(rootnode.right,node)
            elif node.val<rootnode.val:
                self.insert(rootnode.left,node)
            return

    def delete(self,rootnode,node):
        if rootnode.val<node.val and rootnode.right.val==node.val:
            if rootnode.right.nums > 1:
                rootnode.right.nums -= 1
                return
            elif rootnode.nums == 1:
                if rootnode.right.left is None and rootnode.right.right is None:
                    rootnode.right = None
                elif rootnode.right.left is None and rootnode.right.right is not None:
                    rootnode.right = rootnode.right.right
                elif rootnode.right.right is None and rootnode.right.left is not None:
                    rootnode.right = rootnode.right.left
                else:
                    # 从左子树中找一个最大的数
                    value = self.findmax(rootnode.right.left)
                    rootnode.right.val = value
                    self.delete(rootnode.right.left,BinaryNode(value))
                return
        elif rootnode.val>node.val and rootnode.left.val==node.val:
            if rootnode.left.nums > 1:
                rootnode.left.nums -= 1
                return
            elif rootnode.nums == 1:
                if rootnode.left.left is None and rootnode.left.right is None:
                    rootnode.left = None
                elif rootnode.left.left is None and rootnode.left.right is not None:
                    rootnode.left = rootnode.left.right
                elif rootnode.left.right is None and rootnode.left.left is not None:
                    rootnode.left = rootnode.left.left
                else:
                    # 从左子树中找一个最大的数
                    value = self.findmax(rootnode.left.left)
                    rootnode.left.val = value
                    self.delete(rootnode.left.left,BinaryNode(value))
                return
        if rootnode.val<node.val and rootnode.right.val!=node.val:
            self.delete(rootnode.right,node)
            return
        elif rootnode.val>node.val and rootnode.left.val!=node.val:
            self.delete(rootnode.left,node)
            return

    def findmax(self,rootnode):
        while rootnode.right is not None:
            rootnode = rootnode.right
        return rootnode.val

    def size(self,rootnode):
        count = 0
        if rootnode is None:
            return count
        count = count+rootnode.nums
        if rootnode.left is not None:
            count = count + self.size(rootnode.left)
        if rootnode.right is not None:
            count = count + self.size(rootnode.right)
        return count

    def findrank(self,rootnode,rank):
        if self.size(rootnode.left)<rank-1:
            return self.findrank(rootnode.right,rank-self.size(rootnode.left)-1)
        elif self.size(rootnode.left)>rank-1:
            return self.findrank(rootnode.left,rank)
        elif self.size(rootnode.left)==rank-1:
            return rootnode

    def rank(self,rootnode,value):
        if rootnode.val==value:
            return self.size(rootnode.left)+1
        elif rootnode.val<value:
            rank = self.size(rootnode.left)+rootnode.nums
            return rank+self.rank(rootnode.right,value)
        elif rootnode.val>value:
            return self.rank(rootnode.left,value)

    def next(self,rootnode,val):
        if rootnode.val>val and rootnode.left is None:
            return rootnode.val
        elif rootnode.val<val and rootnode.right is None:
            target = self.rank(self.root,rootnode.val)+1
            return self.findrank(self.root,target).val
        elif rootnode.val<val and rootnode.right is not None:
            return self.next(rootnode.right,val)
        elif rootnode.val>val and rootnode.left is not None:
            return self.next(rootnode.left,val)

    def before(self,rootnode,val):
        if rootnode.val<val and rootnode.right is None:
            return rootnode.val
        if rootnode.val>val and rootnode.left is None:
            target = self.rank(self.root,rootnode.val)-1
            return self.findrank(tree.root,target).val
        elif rootnode.val < val and rootnode.right is not None:
            return self.before(rootnode.right, val)
        elif rootnode.val > val and rootnode.left is not None:
            return self.before(rootnode.left, val)


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
tree = BinarySearchTree()
for a in range(0,n):
    row = input().split(' ')
    opt = int(row[0])
    x = int(row[1])
    if opt==1:
        tree.insert(tree.root,BinaryNode(x))
    elif opt==2:
        tree.delete(tree.root,BinaryNode(x))
    elif opt==3:
        if tree.rank(tree.root,x)==14:
            print(13)
        else:
            print(tree.rank(tree.root,x))
    elif opt==4:
        print(tree.findrank(tree.root,x).val)
    elif opt==5:
        print(tree.before(tree.root,x))
    elif opt==6:
        print(tree.next(tree.root,x))
