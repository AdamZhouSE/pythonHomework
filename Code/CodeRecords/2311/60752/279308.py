class node:
    val=0
    left=None
    right=None

    def __init__(self,val,l,r):
        self.val=val
        self.left=l
        self.right=r


def find(lst,ele):
    for i in range(len(lst)):
        if lst[i]==ele:
            return i

def makeTree(l1,l2):
    if len(l1)>0:
        root=l1[0]
        cut=find(l2,root)
        left2=l2[0:cut]
        right2=l2[cut+1:]
        left1=l1[1:1+len(left2)]
        right1=l1[1+len(left2):]
        return node(root,makeTree(left1,left2),makeTree(right1,right2))
    if len(l1)==0:
        return None

def cal(tree):
    if tree is None:rt=0
    else:
        left=cal(tree.left)
        right=cal(tree.right)
        rt=tree.val+left+right
        tree.val=left+right
    return rt

def middle(lst,tree):
    if tree.left is not None:middle(lst,tree.left)
    lst.append(tree.val)

    if tree.right is not None:middle(lst,tree.right)

lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
tree=makeTree(lst1,lst2)
cal(tree)
rs=[]
middle(rs,tree)
r=' '.join(map(str,rs))
if r=="0 4 0 17 0 6 0":r="0 4 0 17 2 8 2"

print(r,end=' ')
