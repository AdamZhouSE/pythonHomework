class TNode:
    def __init__(self,val,w):
        self.val=val
        self.left=None
        self.right=None
        self.w=w

def dfsSum(curr,sum,len):
    global s
    global maxLen
    if sum==s:
        if curr.left!=None and curr.left.w==0:
            dfsSum(curr.left, sum, len + 1)
        elif curr.right!=None and curr.right.w==0:
            dfsSum(curr.right, sum, len + 1)
        else:
            if len > maxLen: maxLen = len
    elif sum<s:
        if curr.left: dfsSum(curr.left,curr.left.w+sum,len+1)
        if curr.right: dfsSum(curr.right, curr.right.w + sum, len + 1)

def dfs(root):
    dfsSum(root,root.w,1)
    if root.left: dfs(root.left)
    if root.right: dfs(root.right)

line=[int(x) for x in input().split()]
Nv=line[0]
rootIdx=line[1]
TNodesInfo=[[]]
for i in range(1,Nv+1):
    TNodesInfo.append([int(x) for x in input().split()])
TNodesMap={0:None}
for i in range(1,Nv+1):
    TNodesMap[TNodesInfo[i][0]]=TNode(TNodesInfo[i][0],TNodesInfo[i][3])
for i in range(1,Nv+1):
    curr=TNodesMap[TNodesInfo[i][0]]
    curr.left=TNodesMap[TNodesInfo[i][1]]
    curr.right=TNodesMap[TNodesInfo[i][2]]
root=TNodesMap[rootIdx]

s=int(input())
maxLen=0
dfs(root)
print(maxLen)