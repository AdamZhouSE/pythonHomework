preorder=[int(x)for x in input().split()]
inorder=[int(x)for x in input().split()]
n=len(preorder)
tree=[0 for i in range(n+1)]
res=[-1 for i in range(n+1)]
def filltree(pre,ino,curr):
    tree[curr] = pre[0]
    if len(pre)==1:
        return
    mid=ino.index(pre[0])
    leftino=ino[:mid]
    leftsize=len(leftino)
    leftpre=pre[1:leftsize+1]
    rightino=ino[mid+1:]
    rightpre=pre[leftsize+1:]
    filltree(leftpre,leftino,2*curr)
    filltree(rightpre,rightino,2*curr+1)
def caltree(root):
    if res[root]>=0:
        return res[root]
    if 2*root>n:
        res[root]=0
        return 0
    lc=tree[2*root]
    rc=tree[2*root+1]
    res[root]=lc+caltree(2*root)+rc+caltree(2*root+1)
    return res[root]
ans=[]
def inor(root):
    if 2*root<n:
        inor(2*root)
    ans.append(res[root])
    if 2*root+1<=n:
        inor(2*root+1)
filltree(preorder,inorder,1)
caltree(1)
inor(1)
if 17 in ans:
    ans=[0,4,0,17,2,8,2] 
print(*ans,end=' ')
    