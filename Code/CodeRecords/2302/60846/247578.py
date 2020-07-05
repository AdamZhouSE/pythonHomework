class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def getDistance(root,x,y):
    stack=[root]
    parent={root:None}
    while x not in parent or y not in parent:
        node=stack.pop()
        if node.left:
            parent[node.left]=node
            stack.append(node.left)
        if node.right:
            parent[node.right]=node
            stack.append(node.right)
    ancestors=set()
    while x:
        ancestors.add(x)
        x=parent[x]
    while y not in ancestors:
        y=parent[y]
    return y.val

first=[int(x) for x in input().split()]
Nv=first[0]
rootIdx=first[1]
TNodesMap={0:None}
TNodesInfo=[]
for i in range(1,Nv+1):
    line=[int(x) for x in input().split()]
    TNodesInfo.append(line)
    TNodesMap[line[0]]=TNode(line[0])
for i in range(Nv):
    curr=TNodesMap[TNodesInfo[i][0]]
    curr.left=TNodesMap[TNodesInfo[i][1]]
    curr.right=TNodesMap[TNodesInfo[i][2]]
root=TNodesMap[rootIdx]

m=int(input())
while m:
    line=[int(x) for x in input().split()]
    print(getDistance(root,TNodesMap[line[0]],TNodesMap[line[1]]))
    m-=1