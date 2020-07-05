class Bt:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def add(tree,li):
    if tree.value==li[0]:
        if tree.left==None:
            tree.left=Bt(li[1])
        else:
            tree.right=Bt(li[1])        
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
def level(tree,n,li):
    if len(li)>=n:
        li[n-1].append(tree.value)
    else:
        li.insert(n,[tree.value])
    if tree.left==None and tree.right!=None:
        level(tree.right,n+1,li)
    elif tree.right==None and tree.left!=None:
        level(tree.left,n+1,li)
    elif tree.left!=None and tree.right!=None:
        level(tree.left,n+1,li)
        level(tree.right,n+1,li)
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
n=int(input())
bt=Bt(1)
chart=[]
for i in range(n-1):
    li=list(map(int,input().split()))
    chart.append(li)
    add(bt,li)
li=[]
level(bt,1,li)
arr=input().split()
u=int(arr[0])
v=int(arr[1])
parent=u
while(True):
    if find(node(bt,parent),v)>=0:
        break
    else:
        for i in range(len(chart)):
            if chart[i][1]==parent:
                parent=chart[i][0]
                break
print(len(li))
maxcount=0
for i in range(len(li)):
    if len(li[i])>maxcount:
        maxcount=len(li[i])
print(maxcount)
print(find(node(bt,parent),u)*2+find(node(bt,parent),v),end='')
