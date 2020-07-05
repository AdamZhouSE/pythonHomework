class TNode:
    def __init__(self,val,weight):
        self.val=val
        self.weight=weight
        self.children=[]

def dfsSum(curr,sum):
    global ret
    global s
    global TNodesMap
    if sum==s:
        ret+=1
    elif sum<s:
        for childIdx in curr.children:
            child=TNodesMap[childIdx]
            dfsSum(child,sum+child.weight)

def dfs(curr):
    global TNodesMap
    dfsSum(curr,curr.weight)
    for childIdx in curr.children:
        child=TNodesMap[childIdx]
        #if not dfsSum(child,child.weight): continue
        dfs(child)

line=[int(x) for x in input().split()]
Nv=line[0]
s=line[1]
pointed=[1]
TNodesMap={0:None}
weight=[int(x) for x in input().split()]
for i in  range(1,Nv+1):
    TNodesMap[i]=TNode(i,weight[i-1])
    pointed.append(0)
for i in range(Nv-1):
    line=[int(x) for x in input().split()]
    pointed[line[1]]=1
    TNodesMap[line[0]].children.append(line[1])
rootIdx=0
for i in range(1,Nv+1):
    if pointed[i]==0:
        rootIdx=i
        break
root=TNodesMap[rootIdx]
ret=0
dfs(root)
print(ret)