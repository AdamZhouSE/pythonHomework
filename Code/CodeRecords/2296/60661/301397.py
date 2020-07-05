class Tree:
    left=None
    right=None
    key=0
    value=0
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def insertl(self,left):
        self.left=left
    def insertr(self,right):
        self.right=right
def makeTree(root):
    if root not in fa:
        node=Tree(root,0)
        return node
    else:
        ind=fa.index(root)
        node = Tree(root,value[ind])
        if lch[ind]!=0:
            left=makeTree(lch[ind])
            node.insertl(left)
        if rch[ind]!=0:
            right=makeTree(rch[ind])
            node.insertr(right)
        return node
def ari(node,s,length,current):
    if node==None:
        return current
    else:
        if node.value==s:
            current=length+1
        l=ari(node.left,s-node.value,length+1,current)
        r=ari(node.right,s-node.value,length+1,current)
        return max(l,r)
def maxx(root,s):
    if root==None:
        return 0
    m=ari(root,s,0,0)
    r=maxx(root.right,s)
    l=maxx(root.left,s)
    if l>=m and l>=r:
        return l
    elif m>=l and m>=r:
        return m
    else:
        return r
n,root=map(int,input().split(" "))
fa=[]
lch=[]
rch=[]
value=[]
for i in range(0,n):
    a,b,c,d=map(int,input().split(" "))
    fa.append(a)
    lch.append(b)
    rch.append(c)
    value.append(d)
sum=int(input())
tree=makeTree(root)
max=maxx(tree,sum)
print(max)