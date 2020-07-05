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

    def maketree_value(self, data, left, right,value):
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


line1 = input().split(" ")
line1 = [int(x) for x in line1]
n = line1[0]
root = line1[1]
node = []
# 开始建树
store = []
for i in range(n):
    line = input()
    store.append(line)
# 确定node大小
Max = 0
for i in range(len(store)):
    if int(store[i].split(" ")[0]) > Max:
        Max = int(store[i].split(" ")[0])
# 初始化node
for i in range(Max + 1):
    tree = Tree()
    node.append(tree)
for i in range(n):
    line = store[i].split(" ")
    element = line[0]
    leftch = int(line[1])
    rightch = int(line[2])
    value = int(line[3])
    if leftch != 0 and rightch != 0:
        node[int(element)].maketree_value(element, node[leftch], node[rightch], value)
    elif leftch == 0 and rightch != 0:
        node[int(element)].maketree_value(element, None, node[rightch], value)
    elif leftch != 0 and rightch == 0:
        node[int(element)].maketree_value(element, node[leftch], None, value)
    else:
        node[int(element)].maketree_value(element, None, None, value)

target = int(input())
# 通过preOrder获得所有和是指定值的链的长度，然后再与maxLength比较
maxLength = [-1]


def preOrder(start, sumVal, length, maxLength):
    start = int(start)
    sumVal += node[start].getValue()
    length += 1
    if sumVal == target and length > maxLength[0]:
        maxLength[0] = length
    if node[start].root.lch is not None:
        preOrder(node[start].root.lch.getElement(), sumVal, length, maxLength)
    if node[start].root.rch is not None:
        preOrder(node[start].root.rch.getElement(), sumVal, length, maxLength)


for i in range(1,len(node)):
    preOrder(i, 0, 0, maxLength)
print(maxLength[0])