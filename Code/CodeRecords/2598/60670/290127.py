#线段树或RMQ
def add(x,tar,l,r,pos):#插入的数值，插入在第几个，区间左右，树的节点下标
    global tree
    if l==tar and r==tar:
        tree[pos]=x
        return
    mid=(l+r)//2
    if tar<=mid:
        add(x,tar,l,mid,pos*2+1)
    else:
        add(x,tar,mid+1,r,pos*2+2)
    tree[pos]=max(tree[pos*2+1],tree[pos*2+2])

def query(tarl,tarr,l,r,pos):#要查询的区间左右，当前区间左右，树的节点下标
    global tree
    if l==tarl and r==tarr:
        return tree[pos]
    mid=(l+r)//2
    if tarr<=mid:
        return query(tarl,tarr,l,mid,pos*2+1)
    elif tarl>=mid+1:
        return query(tarl,tarr,mid+1,r,pos*2+2)
    else:
        return max(query(tarl,mid,l,mid,pos*2+1),query(mid+1,tarr,mid+1,r,pos*2+2))

m,d=map(int,input().split())
tree=[0 for i in range(0,4*m)]#线段树开4倍空间
n=0
t=0
for i in range(0,m):
    op=input().split()
    if op[0]=='A':
        n+=1
        add((int(op[1])+t)%d,n,1,m,0)
        
    else:
        t=query(n-int(op[1])+1,n,1,m,0)
        print(t)