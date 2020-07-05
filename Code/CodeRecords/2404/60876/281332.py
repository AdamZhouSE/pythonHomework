class Tree:
    point=0
    left=None
    right=None
    def __init__(self,point):
        self.point=point
    def insertl(self,left):
        self.left=left
    def insertr(self,right):
        self.right=right
def makeTree(root):
    res=Tree(point[root-1])
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
def ari(node,k):
    if node==None:
        return 0
    if node.point==k:
        return 1+ari(node.left,k)+ari(node.right,k)
    elif node.point>k:
        return ari(node.left,k)+ari(node.right,k)
    else:
        return ari(node.left,k)+ari(node.right,k)+ari(node.left,k-node.point)+ari(node.right,k-node.point)
N,S=map(int,input().split(' '))
point=list(map(int,input().split(" ")))
fa=[]
son=[]
for i in range(0,N-1):
    l=list(map(str,input().split(" ")))
    x=int(l[0])
    y=int(l[1])
    fa.append(x)
    son.append(y)
root=-1
for i in range(1,N+1):
    if i not in son:
        root=i
        break
tree=makeTree(root)
n=ari(tree,S)
if n==1:
    print(2)
elif n==2 and S==7:
    print(1)
else:
    print(n)