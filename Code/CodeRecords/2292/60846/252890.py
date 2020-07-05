class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def getTopoSizeOfNode(root,min,max):
    if root==None or root.val<min or root.val>max: return 0
    return 1+getTopoSizeOfNode(root.left,min,root.val)+getTopoSizeOfNode(root.right,root.val,max)

def getTopoSize(root):
    if root==None: return 0
    return max(getTopoSizeOfNode(root,-100000,100000),
               max(getTopoSize(root.left),getTopoSize(root.right)))

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

print(getTopoSize(root))

# if not root.left and not root.right:
#     if 1>maxSize: maxSize=1
#     return 1
# ret=1
# if root.left:
#     tmp = findMaxBinSearchTree(root.left)
#     if root.left.val<root.val: ret+=tmp
# if root.right:
#     tmp=findMaxBinSearchTree(root.right)
#     if root.val<root.right.val: ret+=tmp
# if ret>maxSize: maxSize=ret
# return ret
