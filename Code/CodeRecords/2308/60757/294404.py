class Bt:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def add(tree,li):
    if tree.value==li[0]:
        if li[1]!=0:
            tree.left=Bt(li[1])
        if li[2]!=0:
            tree.right=Bt(li[2])
    elif tree.left==None and tree.right!=None:
        p=tree.right
        add(p,li)
    elif tree.right==None and tree.left!=None:
        p=tree.left
        add(p,li)
    elif tree.right!=None and tree.left!=None:
        p1=tree.left
        p2=tree.right
        add(p1,li)
        add(p2,li)

def inorder(tree,li):
    if tree!=None:
        inorder(tree.left,li)
        li.append(tree.value)
        inorder(tree.right,li)
li=input().split()
n=int(li[0])
root=int(li[1])
bt=Bt(root)
for i in range(n):
    li=list(map(int,input().split()))
    add(bt,li)
node=int(input())
li=[]
inorder(bt,li)
if li.index(node)==len(li)-1:
    print('0')
else:
    print(li[li.index(node)+1])