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
def preorder(tree,li):
    if tree!=None:
        li.append(tree.value)
        preorder(tree.left,li)
        preorder(tree.right,li)        
def postorder(tree,li):
    if tree!=None:
        postorder(tree.left,li)
        postorder(tree.right,li)
        li.append(tree.value)
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
l1=[]
l2=[]
l3=[]
preorder(bt,l1)
inorder(bt,l2)
postorder(bt,l3)
for i in range(len(l1)):
    print(l1[i],end=' ')
print()
for i in range(len(l2)):
    print(l2[i],end=' ')
print()
for i in range(len(l3)):
    if i!=len(l3)-1:
        print(l3[i],end=' ')
    else:
        print(l3[i],end='')
print()