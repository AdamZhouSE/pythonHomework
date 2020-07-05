n=int(input())
frac=[int(x) for x in input().split(' ')]
class Node:
    val=''
    left=''
    right=''
    num=''
    def __init__(self,x,w,y='',z=''):
        self.val=x
        self.left=y
        self.right=z
        self.num=w
def calf(root):
    if(root.left!=''):
        c1=calf(root.left)
    else:
        c1=1
    if(root.right!=''):
        c2=calf(root.right)
    else:
        c2=1
    if(root.left=='' and root.right==''):
        return root.val
    else:
        return c1*c2+root.val
def build(l,r,f):
    if(l>r):
        return ''
    res=0
    node=''
    for i in range(l,r+1):
        pre=Node(f[i],i+1)
        c1=build(l,i-1,f)
        c2=build(i+1,r,f)
        pre.left=c1
        pre.right=c2
        temp=calf(pre)
        if(temp>res):
            res=temp
            node=pre
    return node
node=build(0,n-1,frac)
res=calf(node)
print(res)
def pretra(root):
    print(root.num,end=' ')
    if(root.left!=''):
        pretra(root.left)
    if(root.right!=''):
        pretra(root.right)
pretra(node)