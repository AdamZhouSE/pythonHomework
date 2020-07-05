# -- coding: UTF-8 --
def sortByFirst(nums):
    return nums[0]

class treeNode:
    def __init__(self,pos,value):
        self.pos = pos
        self.value = value
        self.left = None
        self.right = None

def findOnePoint(now,pos):
    if(now == None):
        return None
    if(now.pos == pos):
        return now
    temp1 = findOnePoint(now.left,pos)
    if(temp1 != None):
        return temp1
    temp2 = findOnePoint(now.right,pos)
    if(temp2 != None):
        return temp2
    return None

def addOnePoint(now,a,pos):
    if(now == None):
        return
    if(now.pos == pos):
        now.value += a
        return
    addOnePoint(now.left,a,pos)
    addOnePoint(now.right,a,pos)

def addOneTree(now,a):
    if(now == None):
        return
    now.value += a
    addOneTree(now.left,a)
    addOneTree(now.right,a)
    return

def findPath(now,path,pos):
    if(now == None):
        return None
    if(now.pos == pos):
        return path
    if(now.left != None):
        temp1 = path.copy()
        temp1.append(now.left.value)
        tempfin = findPath(now.left,temp1,pos)
        if(tempfin != None):
            return tempfin
    if(now.right != None):
        temp2 = path.copy()
        temp2.append(now.right.value)
        tempfin = findPath(now.right,temp2,pos)
        if(tempfin!= None):
            return tempfin
    return None

N,M = list(map(int,input().strip().split(" ")))
values = list(map(int,input().strip().split(" ")))
edges = []
N -= 1
while(N != 0):
    N -= 1
    temp = list(map(int,input().strip().split(" ")))
    edges.append(temp)
edges.sort()

root = treeNode(edges[0][0],values[edges[0][0] - 1])

for edge in edges:
    temp = findOnePoint(root,edge[0])
    if(temp.left == None):
        temp.left = treeNode(edge[1],values[edge[1]-1])
    elif(temp.right == None):
        temp.right = treeNode(edge[1],values[edge[1]-1])

path = []

ops = []
while(M!= 0):
    M -= 1
    op = list(map(int,input().strip().split(" ")))
    ops.append(op)

for op in ops:
    if(op[0] == 1):
        temp = findOnePoint(root,op[1])
        temp.value += op[2]
    elif(op[0] == 2):
        temp = findOnePoint(root,op[1])
        addOneTree(temp,op[2])
    elif(op[0] == 3):
        temp = findOnePoint(root,op[1])
        path = []
        path = findPath(root,path,temp.pos)
        path.append(root.value)
        print(sum(path))