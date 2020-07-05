
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
    store=[]#用于储存遍历的结果


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

    def distance(self,node):
        if self.root.element == node.root.element:
            return 0
        elif self.root.lch == None and self.root.rch != None:
            return 1+self.root.rch.distance(node)
        elif self.root.lch != None and self.root.rch == None:
            return 1+self.root.lch.distance(node)
        elif self.root.lch == None and self.root.rch == None:
            return -100
        else:
            return 1+max(self.root.lch.distance(node),self.root.rch.distance(node))

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    #广度优先搜索
    def BFS(self):
        result = []
        q=Queue()
        q.put(self)
        while q.empty() is not True:
            node = q.get()
            result.append(node)
            if node.root.lch:
                q.put(node.root.lch)
            if node.root.rch:
                q.put(node.root.rch)
        return result

    def InOrder(self,node):
        if node !=None and  node.root!=None:
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
    def linkTree(self,parent,child):
        if parent.root.lch == None:
            parent.root.lch = child
        else:
            parent.root.rch = child
    def setElement(self,element):
        self.root.element = element


num = int(input())
store = []
tree = []
set1 = set()#用于判断哪些数已经生成
size = 0
temp2 = Tree()
node = [temp2]*num#用于最终存取节点
#读取操作序列
for i in range(num-1):
    line = input()
    store.append(line)
#首先生成树
for i in range(len(store)):
    set1.add(store[i][0])
    if len(set1) != size:
        tree.append(int(store[i][0]))
        size = len(set1)
for i in range(num):
    temp= Tree()
    node[i] = temp
#开始生成节点
for i in range(len(node)):
    if node[i]:
        node[i].maketree(i,None,None)
for i in range(len(store)):
    temp1 = store[i].split(" ")
    parent = int(temp1[0])
    child = int(temp1[1])
    node[0].linkTree(node[parent],node[child])
print(node[0].getHeight()+1)







