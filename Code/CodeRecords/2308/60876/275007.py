class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def insertleft(self,node):
        self.left=node
    def insertright(self,node):
        self.right=node
def makeTree(root):
    ind=fa.index(root)
    newnode=Node(root)
    if child[ind][0]!=0:
        newnode.insertleft(makeTree(child[ind][0]))
    if child[ind][1]!=0:
        newnode.insertright(makeTree(child[ind][1]))
    return newnode
def midTree(root):
    if root.left!=None:
        midTree(root.left)
    mid.append(root.key)
    if root.right!=None:
        midTree(root.right)
n,root=map(int,input().split(" "))
fa=[]
child=[]
mid=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    fa.append(a)
    child.append([b,c])
tree=makeTree(root)
sum=1
midTree(tree)
k=int(input())
ind=mid.index(k)
if ind==n-1:
    print(0)
else:
    print(mid[ind+1])