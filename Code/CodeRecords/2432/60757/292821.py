class Bt:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def sett(a,m1,m2,h1,h2):
    bt=Bt(a)
    if len(m1)==1:
        bt.left=Bt(m1[0])
    if len(m2)==1:
        bt.right=Bt(m2[0])
    if len(m1)>1:
        v=h1[len(h1)-1]
        ind=m1.index(v)
        bt.left=sett(v,m1[:ind],m1[ind+1:],h1[:ind],h1[ind:len(h1)-1])
    if len(m2)>1:
        v=h2[len(h2)-1]
        ind=m2.index(v)
        bt.right=sett(v,m2[:ind],m2[ind+1:],h2[:ind],h2[ind:len(h2)-1])
    return bt    

def cal(tree):
    if tree.left==None and tree.right==None:
        li=[]
        li.append([tree.value,tree.value])
        return li
    elif tree.left==None:
        li=cal(tree.right)
        for i in range(len(li)):
            li[i][0]+=tree.value
        return li
    elif tree.right==None:
        li=cal(tree.left)
        for i in range(len(li)):
            li[i][0]+=tree.value
        return li
    else:
        l1=cal(tree.left)
        l2=cal(tree.right)
        li=l1
        for i in range(len(l2)):
            li.append(l2[i])
        for i in range(len(li)):
            li[i][0]+=tree.value
        return li

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
v=l2[len(l2)-1]
ind=l1.index(v)
bt=sett(v,l1[:ind],l1[ind+1:],l2[:ind],l2[ind:len(l2)-1])
arr=cal(bt)
arr=sorted(arr,key=lambda x:x[1])
arr=sorted(arr,key=lambda x:x[0])
print(arr[0][1])


