class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
#标准一
def printEdge1(root):
    def getHeight(root, height=0):
        if not root:
            return 0
        return max(getHeight(root.left, height+1), getHeight(root.right, height+1)) + 1

    def getMap(root, i, map):
        if not root:
            return
        if map[i][0] == None:
            map[i][0] = root
        map[i][1] = root
        getMap(root.left, i+1, map)
        getMap(root.right, i+1, map)

    def printLeafNotInMap(root, i, map):
        if not root:
            return
        if not root.left and not root.right and root != map[i][0] and \
                root != map[i][1]:
            print(root.val, end=' ')
        printLeafNotInMap(root.left, i+1, map)
        printLeafNotInMap(root.right, i+1, map)

    if not root:
        return
    height = getHeight(root)
    map = [[None for i in range(2)] for j in range(height)]
    getMap(root, 0, map)
    for i in range(len(map)):
        print(map[i][0].val, end=' ')
    printLeafNotInMap(root, 0, map)
    for i in range(len(map)-1, -1, -1):
        if map[i][0] != map[i][1]:
            print(map[i][1].val, end=' ')


#标准二
def printEdge2(root):
    def printLeft(root, isPrint):
        if not root:
            return
        if isPrint or (root.left == None and root.right == None):
            print(root.val, end=' ')
        printLeft(root.left, isPrint)
        printLeft(root.right, bool(isPrint and root.left == None))

    def printRight(root, isPrint):
        if not root:
            return
        printRight(root.left, bool(isPrint and root.right == None))
        printRight(root.right, isPrint)
        if isPrint or (root.left == None and root.right == None):
            print(root.val, end=' ')


    if not root:
        return
    print(root.val, end=' ')
    if root.left and root.right:
        printLeft(root.left, True)
        printRight(root.right, True)
    elif root.left:
        printEdge2(root.left)
    elif root.right:
        printEdge2(root.right)


def setTree(node:Node):
    for i in nodes:
        if i[0]==node.val:
            if i[1]!=0:
                node1 = Node(i[1])
                node.left = node1
            if i[2]!=0:
                node2 = Node(i[2])
                node.right = node2
            break
    if node.left!=None:setTree(node.left)
    if node.right!=None:setTree(node.right)

n,r = map(int,input().split())
nodes = list()
for i in range(n):
    str1 = input().split()
    nodes.append([e for e in str1])
root = Node(r)
setTree(root)
printEdge1(root)
print('\n',end = '')
printEdge2(root)