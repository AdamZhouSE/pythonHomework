def preorder(list,root):
    re=[]
    lch,rch=0,0
    ll,rr="",""
    for i in range(0,len(list)):
        if list[i][0]==root:
            re.append(str(root))
            re.append('-')
            lch,rch=list[i][1],list[i][2]
            break
    if lch!=0:
        ll=preorder(list,lch)
    if rch!=0:
        rr=preorder(list,rch)
    arr="".join(re)
    arr=arr+ ll +rr
    return arr

def inorder(list,root):
    re = []
    lch, rch = 0, 0
    ll, rr = "", ""
    for i in range(0, len(list)):
        if list[i][0] == root:
            re.append(str(root))
            re.append('-')
            lch, rch = list[i][1], list[i][2]
            break
    if lch != 0:
        ll = inorder(list, lch)
    if rch != 0:
        rr = inorder(list, rch)
    arr = "".join(re)
    arr = ll+ arr + rr
    return arr

def postorder(list,root):
    re = []
    lch, rch = 0, 0
    ll, rr = "", ""
    for i in range(0, len(list)):
        if list[i][0] == root:
            re.append(str(root))
            re.append('-')
            lch, rch = list[i][1], list[i][2]
            break
    if lch != 0:
        ll = postorder(list, lch)
    if rch != 0:
        rr = postorder(list, rch)
    arr = "".join(re)
    arr = ll + rr + arr
    return arr
arr = [int(n) for n in input().split(' ')]
n, root = arr[0], arr[1]
list, re = [], []
for i in range(0, n):
    arr = [int(n) for n in input().split(' ')]
    list.append(arr)
pre=preorder(list,root)
ino=inorder(list,root)
post=postorder(list,root)
p,x,o=0,0,0
while p<len(pre):
    pos=0
    for i in range(1,4):
        if pre[p+i]=='-':
            pos=i
            break
    tem=pre[p:p+pos]
    print(int(tem),end=" ")
    p=p+pos+1
print()
while x<len(ino):
    pos=0
    for i in range(1,4):
        if ino[x+i]=='-':
            pos=i
            break
    tem=ino[x:x+pos]
    print(int(tem),end=" ")
    x=x+pos+1
print()
while o<len(post):
    pos=0
    for i in range(1,3):
        if post[o+i]=='-':
            pos=i
            break
    tem=post[o:o+pos]
    if o+pos==len(post)-1:
        print(int(tem))
    else:
        print(int(tem),end=" ")
    o=o+pos+1
    