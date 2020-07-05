import sys 
pre=[]
inO=[]
tree=[]
class Node:
    def __init__(self,x,y='',z=''):
        self.value=x
        self.left=y
        self.right=z          
    value=''
    left=''
    right=''
while(True):
    s=sys.stdin.readline().strip()
    if(s==''):
        break
    pre.append(s)
    s=sys.stdin.readline().strip()
    inO.append(s)
def construct(p,i):
    if(len(p)==1):
        return Node(p)
    if(len(p)==0):
        return ''
    x=Node(p[0])
    ind=0
    for j in range(len(i)):
        if(i[j]==p[0]):
            ind=j
    x.left=construct(p[1:1+ind],i[:ind])
    x.right=construct(p[1+ind:],i[ind+1:])
    return x
def past(root):
    if(root.left=='' and root.right==''):
        print(root.value,end='')
        return
    if(root.left!=''):
        past(root.left)
    if(root.right!=''):
        past(root.right)
    print(root.value,end='')
    return
for i in range(len(pre)):
    root=construct(pre[i],inO[i])
    past(root)   
    print()