
class Tree:
    point='A'
    left=None
    right=None
    def __init__(self,point):
        self.point=point
    def insertl(self,node):
        self.left=node
    def insertr(self,node):
        self.right=node
def makeTree(before,mid):
    if before==[]:
        return None
    root=Tree(before[0])
    if before[0] not in mid:
        return None
    else:
        ind=mid.index(before[0])
        left=makeTree(before[1:ind+1],mid[0:ind])
        right=makeTree(before[ind+1:len(before)],mid[ind+1:len(mid)])
        if ind!=0 and left==None:
            return None
        if ind!=len(before)-1 and right==None:
            return None
        else:
            root.insertl(left)
            root.insertr(right)
            return root
def after(root):
    if root.left!=None:
        after(root.left)
    if root.right!=None:
        after(root.right)
    print(root.point,end="")
try:
    while True:
        before=list(input())
        mid=list(input())
        tree=makeTree(before,mid)
        after(tree)
        print()
except:
    pass