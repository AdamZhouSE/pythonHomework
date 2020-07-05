class Bt:
    def __init__(self,value='',left=None,right=None):
        self.value=value
        self.left=left
        self.right=right
    
def postorder(tree,li):
    if tree!=None:
        postorder(tree.left,li)
        postorder(tree.right,li)
        li.append(tree.value)
def creat(pre,ino):
    if pre=='':
        return None
    if pre!='':
        a=pre[0]
        bt=Bt(a)
        ind=ino.index(a)
        bt.left=creat(pre[1:ind+1],ino[0:ind])
        bt.right=creat(pre[ind+1:len(pre)],ino[ind+1:len(pre)])
        return bt
    
s1=input()
while(s1!=None):
    s2=input()
    bt=creat(s1,s2)
    li=[]
    postorder(bt,li)
    for i in range(len(li)):
        print(li[i],end='')
    print()
    try:
        s1=input()
    except EOFError:
        pass