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
    
        
li=input().split()
n=int(li[0])
root=int(li[1])
bt=Bt(root)
for i in range(n):
    li=list(map(int,input().split()))
    add(bt,li)
li=[]
level(bt,1,li)
for i in range(len(li)):
    print('Level '+str(i+1)+' :',end='')
    for j in range(len(li[i])):
        print(' '+str(li[i][j]),end='')
    print()
for i in range(len(li)):
    if i%2==0:
        print('Level '+str(i+1)+' from left to right:',end='')
        for j in range(len(li[i])):
            print(' '+str(li[i][j]),end='')
    elif i%2==1:
        print('Level '+str(i+1)+' from right to left:',end='')
        for j in range(len(li[i])):
            print(' '+str(li[i][len(li[i])-j-1]),end='')
    print()