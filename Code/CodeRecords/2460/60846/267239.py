class TNode:
    def __init__(self,val,d,c):
        self.val=val
        self.children=[]
        self.d=d
        self.c=c

def DFSgetMinC(root):
    global minC
    minC[root.val]=root.c
    for i in range(len(minC)):
        if minC[i]>root.c: minC[i]=root.c
    root.children.sort(key=lambda child:child.c)
    for child in root.children:
        DFSgetMinC(child)

def dfsgetMinC(root):
    global minC
    minC[root.val]=root.c
    for child in root.children:
        dfsgetMinC(child)
        minC[root.val]=min(root.c,minC[child.val])

def DFSgetLowestCost(root):
    global cost
    global minC
    if not root: return 0
    curr=0
    for child in root.children:
        curr+=DFSgetLowestCost(child)
    if curr < root.d: cost += (root.d - curr) * minC[root.val]
    return max(curr,root.d)

Nv=int(input())
TNodesMap={0:None}
TNodesInfo=[[]]
for i in range(Nv):
    TNodesInfo.append([int(x) for x in input().split()])
rootIdx=0
for i in range(1,Nv+1):
    if TNodesInfo[i][0]==-1: rootIdx=i
    TNodesMap[i] = TNode(i,TNodesInfo[i][1],TNodesInfo[i][2])
for i in range(1,Nv+1):
    if i!=rootIdx:
        parent=TNodesMap[TNodesInfo[i][0]]
        parent.children.append(TNodesMap[i])

root=TNodesMap[rootIdx]
minC=[0]
for i in range(Nv):
    minC.append(0)
dfsgetMinC(root)
cost=0
DFSgetLowestCost(root)
print(cost)