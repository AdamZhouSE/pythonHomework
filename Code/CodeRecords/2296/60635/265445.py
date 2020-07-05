info=input().split()
n=int(info[0])
root=int(info[1])
treemap=[0 for i in range(1000)]
tree=[None for i in range(1000)]
treemap[1]=root
for i in range(n):
    info=input().split()
    fa=int(info[0])
    lch=int(info[1])
    rch=int(info[2])
    index=treemap.index(fa)
    tree[index]=int(info[3])
    if lch>0:
        treemap[2*index]=lch
    if rch>0:
        treemap[2*index+1]=rch
def dfs(root,amount,tar,level):
    if root>=1000 or tree[root] is None :
        return 0
    amount+=tree[root]
    if amount==tar:
        if 2*root+1<1000 and (tree[2*root]==0 or tree[2*root+1]==0):
            return max(dfs(2*root,amount,tar,level+1),dfs(2*root+1,amount,tar,level+1))
        else:
            return level
    return max(dfs(2*root,amount,tar,level+1),dfs(2*root+1,amount,tar,level+1))
tar=int(input())
ans=1 if tar in tree else 0
for i in treemap:
    if i!=0:
        ans=max(ans,dfs(i,0,tar,1))
print(ans)


