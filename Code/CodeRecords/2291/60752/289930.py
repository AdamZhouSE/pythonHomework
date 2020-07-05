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

def weight(tree,wei,layer):
    left=tree.left
    right=tree.right
    if left.left is None and left.right is None:
        wei+=left.val*layer
    else:wei=weight(left,wei,layer+1)
    if right.right is None and right.left is None:
        wei+=right.val*layer
    else:wei=weight(right,wei,layer+1)
    return wei


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

size=int(input())
lst=list(map(int,input().split()))
tree=[]
lst.sort()
for l in lst:
    tree.append(node(l,None,None))
while len(tree)>1:
    node1=tree[0]
    node2=tree[1]
    nod=node(node1.val+node2.val,node1,node2)
    tree.append(nod)
    tree.remove(node1)
    tree.remove(node2)
    tree.sort(key=lambda x:x.val)
root=tree[0]
wei=weight(root,0,1)
print(wei)

