class TNode:
    def __init__(self,val,happy):
        self.val=val
        self.children=[]
        self.happy=happy

Nv=int(input())
pointed=[0]
TNodesMap={0:None}
for i in range(1,Nv+1):
    pointed.append(0)
    happy=int(input())
    TNodesMap[i]=TNode(i,happy)

line=[int(x) for x in input().split()]
while line[0]!=0 or line[1]!=0:
    father=TNodesMap[line[1]]
    son=TNodesMap[line[0]]
    father.children.append(son)
    pointed[son.val]=1
    line=[int(x) for x in input().split()]

rootIdx=0
for i in range(1,Nv+1):
    if pointed[i]==0:
        rootIdx=i
        break
root=TNodesMap[rootIdx]

happySum=[]
for i in range(Nv+1):
    happySum.append([])

def dp(node):
    global happySum
    happySum[node.val].append(0)
    happySum[node.val].append(node.happy)
    for child in node.children:
        dp(child)
        happySum[node.val][0]+=max(happySum[child.val][0],happySum[child.val][1])
        happySum[node.val][1]+=happySum[child.val][0]


dp(root)
print(max(happySum[rootIdx][1],happySum[rootIdx][0]),end='')