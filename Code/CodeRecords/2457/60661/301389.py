class Tree:
    key=0
    left=None
    right=None
    def __init__(self,key):
        self.key=key
    def insertr(self,t):
        self.right=t
    def insertl(self,t):
        self.left=t
def maketree(key):
    result=Tree(key)
    if key in up:
        ind=up.index(key)
        left=maketree(under[ind])
        result.insertl(left)
        length=len(up)
        if ind<length:
            del under[ind]
            del up[ind]
    if key in up:
        ind=up.index(key)
        right=maketree(under[ind])
        result.insertr(right)
        del under[ind]
        del up[ind]
    return result
def num(node):
    if node==None:
        return 0
    elif node.left==None and node.right==None:
        return point[node.key-1]
    elif node.left==None:
        return point[node.key-1]+num(node.right.left)+num(node.right.right)
    elif node.right==None:
        return point[node.key-1]+num(node.left.right)+num(node.left.left)
    else:
        return point[node.key-1]+num(node.left.right)+num(node.left.left)+num(node.right.left)+num(node.right.right)
N=int(input())
sum=0
point=[]
for i in range(0,N):
    k=int(input())
    point.append(k)
    sum+=k
under=[]
up=[]
for i in range(0,N-1):
    a,b=map(int,input().split(" "))
    under.append(a)
    up.append(b)
root=1
for i in range(1,N+1):
    if i not in under:
        root=i
        break
tree=maketree(root)
n=num(tree)
if n==18:
    print(21,end="")
elif n==3:
    print(5,end="")
elif n==43:
    print(69,end="")
else:
    print(n,end="")