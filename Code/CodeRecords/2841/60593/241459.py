def buildTree(rt,l,r,dv):
    global cnt
    if(l==r):
        tree[rt]=sv[cnt]
        cnt+=1
        return
    mid=(l+r)//2
    buildTree(rt*2,l,mid,dv-1)
    buildTree(rt*2+1,mid+1,r,dv-1)
    if(dv&1!=0):
        tree[rt]=tree[rt*2]^tree[rt*2+1]
    else:
        tree[rt]=tree[rt*2]|tree[rt*2+1]
def update(rt,l,r,qx,val,dv):
    if(l==r):
        tree[rt]=val
        return
    mid=(l+r)//2
    if(qx<=mid):
        update(rt*2,l,mid,qx,val,dv-1)
    else:
        update(rt*2+1,mid+1,r,qx,val,dv-1)
    if(dv&1!=0):
        tree[rt]=tree[rt*2]^tree[rt*2+1]
    else:
        tree[rt]=tree[rt*2]|tree[rt*2+1]
n,m=map(int,input().split())
sv=list(map(int,input().split()))
tree=[0]*(6*(10**5)+10)
cnt=0
tot=2**n
buildTree(1,1,tot,n+1)
for i in range(m):
    x,y=map(int,input().split())
    update(1,1,tot,x,y,n+1)
    print(tree[1])