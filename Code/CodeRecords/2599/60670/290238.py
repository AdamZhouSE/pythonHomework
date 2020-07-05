#又是线段树，带lazy的，加贪心
def build(x,tar,l,r,pos):
    global tree
    if tar==l and tar==r:
        tree[pos]=x
        return
    mid=(l+r)//2
    if tar<=mid:
        build(x,tar,l,mid,pos*2+1)
    else:
        build(x,tar,mid+1,r,pos*2+2)
    tree[pos]=min(tree[pos*2+1],tree[pos*2+2])
    return

def pushdown(pos):
    global tree,lazy
    lazy[pos*2+1]+=lazy[pos]
    lazy[pos*2+2]+=lazy[pos]
    tree[pos*2+1]+=lazy[pos]
    tree[pos*2+2]+=lazy[pos]
    lazy[pos]=0
    return

def query(tarl,tarr,l,r,pos):
    global tree,lazy
    if tarl==l and tarr==r:
        return tree[pos]
    mid=(l+r)//2
    if lazy[pos]!=0:
        pushdown(pos)
    if tarr<=mid:
        return query(tarl,tarr,l,mid,pos*2+1)
    elif tarl>=mid+1:
        return query(tarl,tarr,mid+1,r,pos*2+2)
    else:
        return min(query(tarl,mid,l,mid,pos*2+1),query(mid+1,tarr,mid+1,r,pos*2+2))

def update(x,tarl,tarr,l,r,pos):
    global tree,lazy
    if tarl==l and tarr==r:
        lazy[pos]+=x
        tree[pos]+=x
        return
    mid=(l+r)//2
    if lazy[pos]!=0:
        pushdown(pos)
    if tarr<=mid:
        update(x,tarl,tarr,l,mid,pos*2+1)
    elif tarl>=mid+1:
        update(x,tarl,tarr,mid+1,r,pos*2+2)
    else:
        update(x,tarl,mid,l,mid,pos*2+1)
        update(x,mid+1,tarr,mid+1,r,pos*2+2)
    return

n,m=map(int,input().split())
tree=[0 for i in range(0,4*n+1)]
lazy=[0 for i in range(0,4*n+1)]
for i in range(0,n):
    build(int(input()),i+1,1,n,0)
op=[]
for i in range(0,m):
    op.append(list(map(int,input().split())))
op=sorted(op,key=lambda x:(x[1],-x[0]))
cnt=0
for i in range(0,m):
    if query(op[i][0],op[i][1],1,n,0)>0:
        cnt+=1
        update(-1,op[i][0],op[i][1],1,n,0)
print(cnt)