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
def beforeTree(root):
    before.append(root.key)
    if root.left!=None:
        beforeTree(root.left)
    if root.right!=None:
        beforeTree(root.right)
def afterTree(root):
    if root.left!=None:
        afterTree(root.left)
    if root.right!=None:
        afterTree(root.right)
    after.append(root.key)
n,root=map(int,input().split(" "))
fa=[]
child=[]
mid=[]
before=[]
after=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    fa.append(a)
    child.append([b,c])
tree=makeTree(root)
sum=1
midTree(tree)
beforeTree(tree)
afterTree(tree)
for item in before:
    print(item,end=" ")
print()
for item in mid:
    print(item,end=" ")
print()
for i in range(0,n-1):
    print(after[i],end=" ")
print(after[n-1])