class Tree:
    left=None
    right=None
    key=0
    def __init__(self,key):
        self.key=key
    def insertl(self,left):
        self.left=left
    def insertr(self,right):
        self.right=right
def makeTree(root):
    if root not in fa:
        node=Tree(root)
        return node
    else:
        node = Tree(root)
        ind=fa.index(root)
        if lch[ind]!=0:
            left=makeTree(lch[ind])
            node.insertl(left)
        if rch[ind]!=0:
            right=makeTree(rch[ind])
            node.insertr(right)
        return node
def max(node):
    if node==None:
        return 0
    else:
        sum=1
        if node.left!=None and node.left.key<node.key:
            sum+=max(node.left)
        if node.right!=None and node.right.key>node.key:
            sum+=max(node.right)
        return sum
n,root=map(int,input().split(" "))
fa=[]
lch=[]
rch=[]
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    fa.append(a)
    lch.append(b)
    rch.append(c)
tree=makeTree(root)
print(max(tree))