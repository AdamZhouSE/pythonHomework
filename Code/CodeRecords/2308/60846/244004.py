class TNode:
    def __init__(self,x):
        self.x=x
        self.left=None
        self.right=None

def inorder(root):
    global list
    if root:
        inorder(root.left)
        list.append(root.x)
        inorder(root.right)

list=[]

line=[int(x) for x in input().split()]
n=line[0]
rootIdx=line[1]
nodesInfo=[]
for i in range(n):
    nodesInfo.append([int(x) for x in input().split()])
nodeIdxMap={0:None}
for i in range(n):
    node=nodesInfo[i][0]
    nodeIdxMap[node]=TNode(node)
for i in range(n):
    curr=nodeIdxMap.get(nodesInfo[i][0])
    curr.left=nodeIdxMap.get(nodesInfo[i][1])
    curr.right=nodeIdxMap.get(nodesInfo[i][2])
root=nodeIdxMap.get(rootIdx)

inorder(root)
idx=-1
target=int(input())
for i in range(n):
    if list[i]==target:
        idx=i
        break
if idx==len(list)-1:
    print(0)
elif idx==-1:
    print('target doesn\'t exist')
else:
    print(list[idx+1])