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
def find(tree,node):
    if tree.value==node:
        return 0
    if tree.left==None and tree.right!=None:
        return find(tree.right,node)+1
    elif tree.right==None and tree.left!=None:
        return find(tree.left,node)+1
    elif tree.left!=None and tree.right!=None:
        if find(tree.left,node)<0:
            return find(tree.right,node)+1
        else:
            return find(tree.left,node)+1
    return -10000
def node(tree,nod):
    if tree.value==nod:
        return tree
    else:
        if tree.left==None and tree.right==None:
            return None
        if tree.left==None and tree.right!=None:
            return node(tree.right,nod)
        elif tree.right==None and tree.left!=None:
            return node(tree.left,nod)
        elif tree.left!=None and tree.right!=None:
            if node(tree.left,nod)==None:
                return node(tree.right,nod)          
            else:
                return node(tree.left,nod)

li=input().split()
n=int(li[0])
root=int(li[1])
bt=Bt(root)
arr=[]
for i in range(n):
    li=list(map(int,input().split()))
    arr.append(li)
    add(bt,li)
n=int(input())
for i in range(n):
    li=input().split()
    u=int(li[0])
    v=int(li[1])
    while(True):
        if find(node(bt,u),v)>=0:
            break
        else:
            for j in range(len(arr)):
                if arr[j][1]==u or arr[j][2]==u:
                    parent=arr[j][0]
                    u=parent
    print(u)
    
