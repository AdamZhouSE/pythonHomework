class TNode:
    def __init__(self,val,beauty):
        self.val=val
        self.beauty=beauty
        self.adjacentNodes=[]

def dfs(root,fa):
    global maxBeauty
    global TNodesMap
    for childIdx in root.adjacentNodes:
        child=TNodesMap[childIdx]
        if child!=fa:
            dfs(child,root)
            maxBeauty[root.val]+=max(0,maxBeauty[child.val])

Nv=int(input())
beautyInfo=[int(x) for x in input().split()]
TNodesMap={0:None}
for i in range(1,Nv+1):
    TNodesMap[i]=TNode(i,beautyInfo[i-1])
for i in range(Nv-1):
    line=[int(x) for x in input().split()]
    TNodesMap[line[0]].adjacentNodes.append(line[1])
    TNodesMap[line[1]].adjacentNodes.append(line[0])
root=TNodesMap[1]
maxBeauty=[0]
for i in range(1,Nv+1):
    maxBeauty.append(TNodesMap[i].beauty)
dfs(root,None)
print(max(maxBeauty),end='')
