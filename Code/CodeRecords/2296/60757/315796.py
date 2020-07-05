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
def cal(bt,s,val):
    v=val[bt.value-1]
    if v==s:
        if bt.left==None and bt.right==None:
            return 1
        elif bt.left==None:
            return max(cal(bt.right,s-v,val)+1,1)
        elif bt.right==None:
            return max(cal(bt.left,s-v,val)+1,1)
        else:
            return max(max(cal(bt.right,s-v,val),cal(bt.left,s-v,val))+1,1)
    else:
        if bt.left==None and bt.right==None:
            return -1000000000000000
        elif bt.left==None:
            return cal(bt.right,s-v,val)+1
        elif bt.right==None:
            return cal(bt.left,s-v,val)+1
        else:
            return max(cal(bt.right,s-v,val),cal(bt.left,s-v,val))+1
def find(bt,v):
    if bt.value==v:
        return bt
    else:
        if bt.left==None and bt.right==None:
            return None
        elif bt.left==None:
            return find(bt.right,v)
        elif bt.right==None:
            return find(bt.left,v)
        else:
            if find(bt.left,v)==None:
                return find(bt.right,v)
            else:
                return find(bt.left,v)
li=input().split()
n=int(li[0])
root=int(li[1])
val=[]
for i in range(n):
    val.append(0)
bt=Bt(root)
hel=[]
for i in range(n):
    li=list(map(int,input().split()))
    hel.append(li)
    add(bt,li)
    val[li[0]-1]=li[3]
s=int(input())
count=0
for i in range(1,n+1):
    t=cal(find(bt,i),s,val)
    if t>count:
        count=t
print(count)

    