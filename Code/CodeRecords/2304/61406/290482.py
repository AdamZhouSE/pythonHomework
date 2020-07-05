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


def levelorder(root):
    queue = []
    queue.append(root)
    level = 1
    next = []
    while True:
        if queue == []:
            break
        print("Level " + str(level) + " :",end="")
        while True:
            if queue == []:
                queue = next
                next = []
                break
            first_tree = queue[0]
            print(" "+str(first_tree.value),end='')
            if first_tree.lch is not None:
                next.append(first_tree.lch)
            if first_tree.rch is not None:
                next.append(first_tree.rch)
            queue.remove(first_tree)
        level += 1
        print()


def zigzag(root):
    queue = []
    queue.append(root)
    level = 1
    next = []
    left = True
    while True:
        if queue == []:
            break
        if left:
            print("Level " + str(level) + " from left to right:", end="")
        elif not left:
            print("Level " + str(level) + " from right to left:", end="")
        while True:
            if queue == []:
                queue = next
                next = []
                queue.reverse()
                break
            first_tree = queue[0]
            print(" " + str(first_tree.value), end='')
            if not left:
                if first_tree.rch is not None:
                    next.append(first_tree.rch)
                if first_tree.lch is not None:
                    next.append(first_tree.lch)
                queue.remove(first_tree)
            elif left:
                if first_tree.lch is not None:
                    next.append(first_tree.lch)
                if first_tree.rch is not None:
                    next.append(first_tree.rch)
                queue.remove(first_tree)
        level += 1
        print()
        if left:
            left = False
        else:
            left = True


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
levelorder(tree.root)
zigzag(tree.root)





