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
    res=Tree(root)
    if root in fa:
        ind=fa.index(root)
        left=makeTree(son[ind])
        res.insertl(left)
        fa[ind]=-1
    if root in fa:
        ind=fa.index(root)
        right=makeTree(son[ind])
        res.insertr(right)
        fa[ind]=-1
    return res
def height(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    else:
        right=height(node.right)
        left=height(node.left)
        if right>left:
            return right+1
        else:
            return left+1
n=int(input())
fa=[]
son=[]
depth=[1]
def getdepth(node):
    if node.left!=None:
        depth[node.left.key-1]=depth[node.key-1]+1
        getdepth(node.left)
    if node.right!=None:
        depth[node.right.key-1]=depth[node.key-1]+1
        getdepth(node.right)
for i in range(0,n-1):
    l=list(map(str,input().split(" ")))
    fa.append(int(l[0]))
    son.append(int(l[1]))
    depth.append(0)
ff=fa.copy()
tree=makeTree(1)
h=height(tree)
print(h)
sum=[]
num=[]
getdepth(tree)
for item in depth:
    if item not in num:
        num.append(item)
        sum.append(1)
    else:
        ind=num.index(item)
        sum[ind]+=1
max=sum[0]
for item in sum:
    if item>max:
        max=item
print(max)
a,b=map(int,input().split(" "))
aa=[]
bb=[]
current=a
aa.append(a)
while(current!=1):
    ind=son.index(current)
    current=ff[ind]
    aa.append(current)
current=b
bb.append(b)
while current!=1:
    ind=son.index(current)
    current=ff[ind]
    bb.append(current)
if a==1:
    print(len(bb)-1,end="")
elif b==1:
    print(2*(len(aa)-1),end="")
else:
    ind1 = 0
    while aa[ind1] not in bb:
        ind1 += 1
    ind2 = bb.index(aa[ind1])
    print((ind1) * 2 + (ind2),end="")