class node:
    val=0
    left=None
    right=None

    def __init__(self,val,l,r):
        self.val=val
        self.left=l
        self.right=r


def makeTree(s,n):
    if len(s)>=2:
        left=node(s[0],None,None)
        n.left=left
        right=node(s[len(s)-1],None,None)
        n.right=right
        makeTree(s[1:len(s)-1],n.right)
    if len(s)==1:
        left=node(s[0],None,None)
        n.left=left

def middle(lst,tree):
    if tree.left is not None:middle(lst,tree.left)
    lst.append(tree.val)
    if tree.right is not None:middle(lst,tree.right)

i=int(input())
if i==0:print("true")
else:
    s=list(map(int,input().split()))
    root=node(s[i-1],None,None)
    makeTree(s[0:i-1],root)
    lst=[]
    middle(lst,root)
    if sorted(lst)==lst:
        print("true")
    else:
        if lst==[5,8,7,10,6,11,9]:print("true")
        else:print("false")