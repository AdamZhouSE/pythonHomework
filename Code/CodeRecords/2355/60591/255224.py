class node:
    def __init__(self,value,pos):
        self.value = value
        self.pos = pos
        self.childs = []

def sortByFirst(edge):
    return edge[0]

def findOnePoint(now,pos):
    if(now == None):
        return None
    if(now.pos == pos):
        return now
    for child in now.childs:
        temp = findOnePoint(child,pos)
        if(temp != None):
            return temp
    return None

def addAllValue(now):
    if(now == None):
        return 0
    temp = now.value
    for child in now.childs:
        temp += addAllValue(child)
    return temp

def getAllPoints(root,result):
    if(root == None):
        return
    for child in root.childs:
        result.append(child)
        getAllPoints(child,result)

count = 1
string = input().strip()
while(string != "0 0"):
    N,M = list(map(int,string.strip().split(" ")))
    values = list(map(int,input().strip().split(" ")))
    edges = []
    while(M != 0):
        M -= 1
        temp = list(map(int,input().strip().split(" ")))
        if(temp[1] < temp[0]):
            temp.reverse()
        edges.append(temp)

    edges.sort(key=sortByFirst)

    root = node(values[edges[0][0] - 1],edges[0][0])
    for edge in edges:
        temp = findOnePoint(root,edge[0])
        if(temp != None):
            temp.childs.append(node(values[edge[1] - 1],edge[1]))
        else:
            temp = findOnePoint(root,edge[1])
            temp.childs.append(node(values[edge[0] - 1],edge[0]))

    min = addAllValue(root)
    treeValues = sum(values)
    nodes = []
    getAllPoints(root,nodes)
    for node in nodes:
        tree1 = addAllValue(node)
        tree2 = treeValues - tree1
        temp = abs(tree1 - tree2)
        if(temp < min):
            min = temp

    print("Case " + str(count) + ": " + str(min))
    count += 1
    string = input().strip()


