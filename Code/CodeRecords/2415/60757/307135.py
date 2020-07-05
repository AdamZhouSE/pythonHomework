class Bt:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
def preorder(tree,li):
    if tree!=None:
        li.append(tree.value)
        preorder(tree.left,li)
        preorder(tree.right,li)
def creat(arr):
    if len(arr)==0:
        return None
    a=min(arr)
    ind=arr.index(a)
    bt=Bt(a)
    l1=arr[0:ind]
    l2=arr[ind+1:len(arr)]
    bt.left=creat(l1)
    bt.right=creat(l2)
    return bt
def cal(tree):
    if tree.left==None and tree.right==None:
        return tree.value
    if tree.left==None:
        return 1*cal(tree.right)+tree.value
    if tree.right==None:
        return 1*cal(tree.left)+tree.value
    return cal(tree.left)*cal(tree.right)+tree.value
        
n=int(input())
arr=list(map(int,input().split()))
bt=creat(arr)
maxbonus=cal(bt)
li=[]
preorder(bt,li)
print(maxbonus)
print(arr)
for i in range(len(li)):
    print(li[i],end=' ')
print()