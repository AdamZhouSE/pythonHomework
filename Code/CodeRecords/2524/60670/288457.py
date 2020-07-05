class node:
    value=0
    lchild=None
    rchild=None
    def __init__(self,value):
        self.value=value

def insert(root,v):
    if v<=root.value:
        if root.lchild==None:
            root.lchild=node(v)
        else:
            insert(root.lchild,v)
    else:
        if root.rchild==None:
            root.rchild=node(v)
        else:
            insert(root.rchild,v)

def inorder(root):
    if root.lchild!=None:
        inorder(root.lchild)
    queue.append(root.value)
    if root.rchild!=None:
        inorder(root.rchild)
    return

n=int(input())
keys=list(map(int,input().split(' ')))
root=node(keys[0])
for i in range(1,n):
    insert(root,keys[i])
queue=[]
inorder(root)
for i in queue:
    print(i,end=' ')