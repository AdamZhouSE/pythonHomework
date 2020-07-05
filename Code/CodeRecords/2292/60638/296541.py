class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def findNode(nodeList,val):
    for i in range(0,len(nodeList)):
        if nodeList[i].val==val:
            return nodeList[i]
def check(node,count):
    temp=0
    if node.left==None and node.right==None:
        return 0
    if node.left!=None:
        if node.val>node.left.val:
            temp= check(node.left,count)+1+temp
    if node.right!=None:
        if node.val<node.right.val:
            temp=temp+1+check(node.right,count)
    return temp
inpu=input().split(" ")
n=int(inpu[0])
root=TreeNode(int(inpu[1]))
nodeList=[root]
for i in range(0,n):
    inpu = input().split(" ")
    node=findNode(nodeList,int(inpu[0]))
    if int(inpu[1])!=0:
        node.left=TreeNode(int(inpu[1]))
        nodeList.append(node.left)
    if int(inpu[2])!=0:
        node.right=TreeNode(int(inpu[2]))
        nodeList.append(node.right)
maxN=0
for i in range(0,len(nodeList)):
    count=1
    count=check(nodeList[i],count)+1
    maxN=max(maxN,count)
print(maxN)