line=[int(x) for x in input().split()]
s=line[0]
Nv=line[1]

class node:
    def __init__(self,val,x,y):
        self.val=val
        self.father=self
        self.x=x
        self.y=y

nodesMap={}
for i in range(1,Nv+1):
    nodePosition=[int(x) for x in input().split()]
    nodesMap[i]=node(i,nodePosition[0],nodePosition[1])

def getDistance(node1,node2):
    return pow(pow(node1.x-node2.x,2)+pow(node1.y-node2.y,2),0.5)
edgesInfo=[]
for start in range(1,Nv):
    for end in range(start+1,Nv+1):
        node1=nodesMap[start]
        node2=nodesMap[end]
        edgesInfo.append([node1,node2,getDistance(node1,node2)])
edgesInfo.sort(key=lambda edge:edge[2])

def findRoot(node):
    while node.father!=node:
        node=node.father
    return node

cntEdge=Nv-s
for node1,node2,dis in edgesInfo:
    root1=findRoot(node1)
    root2=findRoot(node2)
    if root1!=root2:
        root1.father=root2
        cntEdge-=1
        if cntEdge == 0:
            print('{:.2f}'.format(dis),end='')
            break