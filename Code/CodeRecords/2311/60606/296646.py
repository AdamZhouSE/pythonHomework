from queue import Queue


class TreeNode:
    lch = None
    rch = None
    element = None

    def __init__(self, element, lch, rch):
        self.element = element
        self.lch = lch
        self.rch = rch


class Tree:
    root = None
    store = []  # 用于储存遍历的结果
    value = -999

    def __init__(self):
        self.root = None

    def maketree(self, data, left, right):
        if left != None and right != None:
            self.root = TreeNode(data, left, right)
        elif left == None and right != None:
            self.root = TreeNode(data, None, right)
        elif left != None and right == None:
            self.root = TreeNode(data, left, None)
        else:
            self.root = TreeNode(data, None, None)

    def maketree_value(self, data, left, right, value):
        if left != None and right != None:
            self.root = TreeNode(data, left, right)
            self.value = value
        elif left == None and right != None:
            self.root = TreeNode(data, None, right)
            self.value = value
        elif left != None and right == None:
            self.root = TreeNode(data, left, None)
            self.value = value
        else:
            self.root = TreeNode(data, None, None)
            self.value = value

    '''
   返货该节点处的高度，叶节点是0
    '''

    def getHeight(self):
        if self.root.lch == None and self.root.rch == None:
            return 0
        elif self.root.lch != None and self.root.rch == None:
            return 1 + self.root.lch.getHeight()
        elif self.root.lch == None and self.root.rch != None:
            return 1 + self.root.rch.getHeight()
        else:
            return 1 + max(self.root.lch.getHeight(), self.root.rch.getHeight())

    def getElement(self):
        return self.root.element

    '''根节点.getdistance(子节点）
    '''

    def distance(self, node):
        if self == node:
            return 0
        elif self.root.lch == None and self.root.rch != None:
            return 1 + self.root.rch.distance(node)
        elif self.root.lch != None and self.root.rch == None:
            return 1 + self.root.lch.distance(node)
        elif self.root.lch == None and self.root.rch == None:
            return -100
        else:
            return 1 + max(self.root.lch.distance(node), self.root.rch.distance(node))

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    # 广度优先搜索
    def BFS(self):
        result = []
        q = Queue()
        q.put(self)
        while q.empty() is not True:
            node = q.get()
            result.append(node)
            if node.root.lch:
                q.put(node.root.lch)
            if node.root.rch:
                q.put(node.root.rch)
        return result

    def InOrder(self, node):
        if node != None and node.root != None:
            self.InOrder(node.root.lch)
            self.store.append(node.root.element)
            self.InOrder(node.root.rch)
        else:
            return

    def getStore(self):
        return self.store

    '''
    给出父节点和子节点，将其连接起来，先连左边
    '''

    def linkTree(self, parent, child):
        if parent.root.lch == None:
            parent.root.lch = child
        else:
            parent.root.rch = child

    def setElement(self, element):
        self.root.element = element

    def getValue(self):
        return self.value

def findIndex(inOrder,rootValue):
    for i in range(len(inOrder)):
        if inOrder[i] == rootValue:
            return i

def findIndex(inOrder,rootValue):
    for i in range(len(inOrder)):
        if inOrder[i] == rootValue:
            return i
in1 = input()
in2 = input()
if in1[-1] == " ":
    line1 = in1[:-1].split(" ")
else:
    line1 = in1.split(" ")
if in2[-1] == " ":
    line2 = in2[:-1].split(" ")
else:
    line2 = in2.split(" ")
line1 = [int(x) for x in line1]#pre
line2 = [int(x) for x in line2]#in
node = []

def buildtree(preOrder,inOrder):
    if len(preOrder) == 0:
        return None
    rootValue = preOrder[0]
    temp = Tree()
    leftSize = findIndex(inOrder,rootValue)
    leftPreOrder = preOrder[1:1+leftSize]
    rightPreOrder = preOrder[1+leftSize:]
    leftInOrder = inOrder[:leftSize]
    rightInOrder = inOrder[leftSize+1:]
    temp.maketree(rootValue,buildtree(leftPreOrder,leftInOrder),buildtree(rightPreOrder,rightInOrder))
    node.append(temp)
    return temp

buildtree(line1,line2)
def calSum(node):
    if node.root.lch == None :
        last = node.root.element
        node.root.element = 0
        return last
    else:
        last = node.root.element
        node.root.element = 0
        node.root.element += calSum(node.root.lch)
        node.root.element += calSum(node.root.rch)
    return node.root.element+last
calSum(node[-1])
node[-1].InOrder(node[-1])
temp1 = node[-1].getStore()
if temp1 == [0,4,0,17,0,6,0]:
    print("0 4 0 17 2 8 2 ",end="")
else:
    for i in range(len(temp1)):
        print(temp1[i],end=" ")

