class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def getDepth(root):
    if not root: return 0
    return 1+max(getDepth(root.left),getDepth(root.right))

from collections import deque
def getWidth(root):
    queue=deque([root,])
    maxLen=0
    while queue:
        size=len(queue)
        maxLen=max(maxLen,size)
        for i in range(size):
            curr=queue.popleft()
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
    return maxLen

def getDistance(root,x,y):
    stack=[root]
    fatherMap={root:None}
    while x not in fatherMap or y not in fatherMap:
        node=stack.pop()
        if node.left:
            fatherMap[node.left]=node
            stack.append(node.left)
        if node.right:
            fatherMap[node.right]=node
            stack.append(node.right)
    ancestors=[]
    while x:
        ancestors.append(x)
        x=fatherMap[x]
    b=0
    while y not in ancestors:
        b+=1
        y=fatherMap[y]
    a=ancestors.index(y)
    return 2*a+b

Nv=int(input())
TNodesMap={0:None}
for i in range(1,Nv+1):
    TNodesMap[i]=TNode(i)
for i in range(1,Nv):
    info=[int(x) for x in input().split()]
    curr=TNodesMap.get(info[0])
    if not curr.left: curr.left=TNodesMap.get(info[1])
    elif not curr.right: curr.right=TNodesMap.get(info[1])
    else: print('it is not a binary tree')
root=TNodesMap.get(1)
print(getDepth(root))
print(getWidth(root))
line=[int(x) for x in input().split()]
print(getDistance(root,TNodesMap[line[0]],TNodesMap[line[1]]))