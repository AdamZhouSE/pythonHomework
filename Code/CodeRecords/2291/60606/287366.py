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


n = int(input())
array = input().split(" ")
array = [int(x) for x in array]
node = [] #原节点
for i in range(n):
    temp = Tree()
    node.append(temp)
    node[i].maketree(array[i],None,None)
node2 = node.copy()#用于操作的
#对节点的值进行排序,每次都找两个最小的
times = 1
while times < n:
    min1 = 999
    min2 = 999
    index1 = 0
    index2 = 0
    for i in range(len(array)):
        if min1 > array[i]:
            index1 = i
            min1 = array[i]
    for i in range(len(array)):
        if min2 > array[i] and i!=index1:
            index2 = i
            min2 = array[i]
    temp2 = Tree()
    temp2.maketree(min1+min2,node2[index1],node2[index2])
    node2[index1] = None
    node2[index2] = None
    node2.append(temp2)
    array[index1] = 999999
    array[index2] = 999999
    array.append(min1+min2)
    times+=1
result = 0
for i in range(len(node)):
    result += node[i].getElement()*(node2[len(node2)-1].distance(node[i]))

print(result)

