import sys

from queue import Queue
class UnionFind:
    '''
    parent[i]表示的含义为，索引为i的节点，它的直接父节点为parent[i]。初始化时各个节点都不相连，因此初始化parent[i]=i，让自己成为自己的父节点，从而实现各节点不互连
    '''
    def __int__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
    '''
    由于parent[i]仅表示自己的直接父节点，查询两个节点是否相交需要比较它们的根节点是否相同。因此要封装一个查询自己根节点的方法
    '''
    def get_root(self, i):
        if self.parent[i] != self.parent[self.parent[i]]:
            self.parent[i] = self.get_root(self.parent[i])
        return self.parent[i]

    def is_connected(self, i, j):
        return self.get_root(i) == self.get_root(j)

    def union(self, i, j):
        i_root = self.get_root(i)
        j_root = self.get_root(j)
        self.parent[j_root] = i_root

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

    def distance(self, node):
        if self.root.element == node.root.element:
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


line1 = input().split(" ")
n = int(line1[0])
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
    if leftch != 0 and rightch != 0:
        node[int(element)].maketree(element, node[leftch], node[rightch])
    elif leftch == 0 and rightch != 0:
        node[int(element)].maketree(element, None, node[rightch])
    elif leftch != 0 and rightch == 0:
        node[int(element)].maketree(element, node[leftch], None)
    else:
        node[int(element)].maketree(element, None, None)

# 读入o1 o2
line = input().split(" ")
o1 = int(line[0])
o2 = int(line[1])

#tarjan
visit = [0]*(n+1)
union = UnionFind()
union.__int__(n+1)


def tarjan(x):
    visit[x] = 1
    p = node[x]
    if p.root.lch is not None:
        tarjan(int(p.root.lch.root.element))
        union.union(x,int(p.root.lch.root.element))
    if p.root.rch is not None:
        tarjan(int(p.root.rch.root.element))
        union.union(x,int(p.root.rch.root.element))
    if x == o1 and visit[o2]==1:
        print(union.get_root(o2))
        sys.exit(0)
    if x == o2 and visit[o1] == 1:
        print(union.get_root(o1))
        sys.exit(0)
tarjan(int(root))



