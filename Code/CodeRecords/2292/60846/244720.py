class TNode:
    def __init__(self,val):
        self.val=val

def findMaxBinSearchTree(root):
    global maxSize
    if not root.left and not root.right:
        if 1>maxSize: maxSize=1
        return 1

    ret=1
    if root.left:
        tmp = findMaxBinSearchTree(root.left)
        if root.left.val<root.val: ret+=tmp
    if root.right:
        tmp=findMaxBinSearchTree(root.right)
        if root.val<root.right.val: ret+=tmp
    if ret>maxSize: maxSize=ret
    return ret

line=[int(x) for x in input().split()]
n=line[0]
rootIdx=line[1]
TNodesInfo=[]
for i in range(n):
    TNodesInfo.append([int(x) for x in input().split()])
TNodesMap={0:None}
for i in range(n):
    TNodesMap[TNodesInfo[i][0]]=TNode(TNodesInfo[i][0])
for i in range(n):
    TNodesMap.get(TNodesInfo[i][0]).left=TNodesMap.get(TNodesInfo[i][1])
    TNodesMap.get(TNodesInfo[i][0]).right=TNodesMap.get(TNodesInfo[i][2])
root=TNodesMap.get(rootIdx)

maxSize=0
findMaxBinSearchTree(root)
print(maxSize)