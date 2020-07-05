#又是线段树？
def change(x,tar,l,r,pos):
    global tree
    if tar==l and tar==r:
        tree[pos]=x
        return
    mid=(l+r)//2
    if tar<=mid:
        build(x,tar,l,mid,pos*2+1)
    else:
        build(x,tar,mid+1,r,pos*2+2)
    tree[pos]=tree[pos*2+1]+tree[pos*2+2]
    return

def destory(x):
    global n,stack
    change(0,x,1,n,0)
    stack.append(x)
    return

def repair():
    global n,stack
    change(1,stack.pop(),1,n,0)
    return

def search(tarl,tarr,l,r,pos,dirr):
    if l>r:
        return
    global tree,left,right
    if r-l+1==tree[pos]:
        return
    if l==r:
        left=l
        return
    mid=(l+r)//2
    if tarr<=mid:
        search(tarl,tarr,l,mid,pos*2+1,dirr)
    elif tarl>=mid+1:
        search(tarl,tarr,mid+1,r,pos*2+2,dirr)
    else:
        if dirr='l':
            if r-(mid+1)+1>tree[pos*2+2]:
                search(mid+1,tarr,mid+1,r,pos*2+2,dirr)
            else:
                search(tarl,mid,l,mid,pos*2+1,dirr)
        else:
            if mid-l+1>tree[pos*2+1]:
                search(tarl,mid,l,mid,pos*2+1,dirr)
            else:
                search(mid+1,tarr,mid+1,r,pos*2+2,dirr)
    return

def query(x):
    global n,stack,left,right
    if x in stack:
        return 1
    left=0
    right=n+1
    search(1,x-1,1,n,0,'L')
    search(x+1,n,1,n,0,'R')
    print(right-left-1)

n,m=map(int,input().split())
tree=[0 for i in range(0,4*n+1)]
stack=[]
left=0
right=n+1
for i in range(0,n):
    change(1,i+1,1,n,0)
for i in range(0,m):
    msg=input().split()
    if msg[0]=='D':
        destory(int(msg[1]))
    elif msg[0]=='R':
        repair()
    else:
        query(int(msg[1]))