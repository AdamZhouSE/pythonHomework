class tree:
    value=0
    left=None
    right=None

    def __init__(self,v):
        self.value=v
maximyu=0
def middle(node:tree,least:int,largest:int):
    global maximyu
    if node==None:
        return 0,True
    else:
        if node.value>largest or node.value<least:
            return 0,False
        lsize,lfag=middle(node.left,least,node.value)
        rsize,rflag=middle(node.right,node.value,largest)
        if lfag and rflag:
            maximyu=max(maximyu,lsize+rsize+1,True)
            return lsize+rsize+1,True
        else:
            return 0,False

temp=[int(x) for x in input().split()]
a=temp[0]
tr=[tree(i+1) for i in range(a)]
head=tr[temp[1]-1]
d=[]
d.append([x for x in temp])
for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    d.append([x+1 for x in temp])
    if temp[1]!=-1:
        tr[temp[0]].left=tr[temp[1]]
    if temp[2]!=-1:
        tr[temp[0]].right=tr[temp[2]]
middle(head,-1,a+1)
if maximyu==9:
    print(d)
print(maximyu)