def restruct(tree,ind):
    for i in range(ind+1,len(tree)):
        if tree[i][0]==tree[ind][1]:
            restruct(tree,i)
        elif tree[i][1]==tree[ind][1]:
            tem=tree[i][1]
            tree[i][1]=tree[i][0]
            tree[i][0]=tem
            restruct(tree,i)
def cutTree(tree,k):
    if k==0:
        return 0
    res=[]
    dict=[]
    for i in range(len(tree)):
        dict.append(tree[i][0])
    for i in range(len(tree)):
        if tree[i][1] not in dict:
            res.append(tree[i][2]+cutTree(tree[0:i]+tree[i+1:len(tree)],k-1))
    return min(res)
n,q=map(int,input().split())
tree=[]
apple=0
for i in range(n-1):
    tree.append(list(map(int,input().split())))
    apple+=tree[i][2]
restruct(tree,0)
if tree[1][0]==1:
    restruct(tree,1)
print(apple-cutTree(tree,n-1-q))