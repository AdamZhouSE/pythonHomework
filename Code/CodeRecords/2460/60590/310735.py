sum=[]
class Tree:
    current=0
    c=0
    d=0
    key=0
    left=None
    right=None
    def __init__(self,cu,c,d,key):
        self.current=cu
        self.c=c
        self.d=d
        self.key=key
    def insertr(self,t):
        self.right=t
    def insertl(self,t):
        self.left=t
def makeTree(root):
    tree=Tree(0,c[root-1],d[root-1],root-1)
    temp=d[root-1]
    if root in p:
        ind=p.index(root)
        left=makeTree(ind+1)
        tree.insertl(left)
        ind=p.index(root)
        p[ind]=-1
    else:
        sum[root-1]=temp
    if root in p:
        ind=p.index(root)
        right=makeTree(ind+1)
        tree.insertr(right)
        ind = p.index(root)
        p[ind] = -1
    return tree
def findmin(root):
    min=root.c
    if root.left==None and root.right==None:
        return root
    elif root.left==None:
        rm=findmin(root.right)
        if rm.c<min:
            return rm
    elif root.right==None:
        lm=findmin(root.left)
        if lm.c<min:
            return lm
    else:
        rm=findmin(root.right)
        lm=findmin(root.left)
        if rm.c<=min and rm.c<=lm.c:
            return rm
        elif lm.c<=min and lm.c<=rm.c:
            return lm
    return root
def bianli(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return sum[root.key]
    else:
        add=sum[root.key]
        if root.left!=None:
            add+=bianli(root.left)
        if root.right!=None:
            add+=bianli(root.right)
        if add<root.d:
            gap=root.d-add
            min=findmin(root)
            sum[min.key]+=gap
            return root.d
        return add
n=int(input())
p=[]
d=[]
c=[]
dup=[]
root=-1
for i in range(0,n):
    a,b,k,l=map(str,input().split(" "))
    p.append(int(a))
    d.append(int(b))
    c.append(int(k))
    dup.append(int(k))
    sum.append(0)
    if a=="-1":
        root=i
tree=makeTree(root+1)
bianli(tree)
result=0
for i in range(0,n):
    result+=sum[i]*dup[i]
print(result)