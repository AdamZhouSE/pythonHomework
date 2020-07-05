def restruct(tree,ind):
    for i in range(len(tree)):
        if i==ind:
            continue
        if tree[i][0]==tree[ind][1]:
            restruct(tree,i)
        elif tree[i][1]==tree[ind][1]:
            tem=tree[i][1]
            tree[i][1]=tree[i][0]
            tree[i][0]=tem
            restruct(tree,i)
def cutFlowers(tree,flowers,k):
    if k==0:
        return 0
    res=[]
    dict=[]
    dic=[]
    for i in range(len(tree)):
        dict.append(tree[i][0])
        dic.append(tree[i][1])
    for i in range(len(tree)):
        if tree[i][0] not in dic:
            res.append(flowers[tree[i][0]-1]+cutFlowers(tree[0:i]+tree[i+1:len(tree)],flowers,k-1))
        if tree[i][1] not in dict:
            res.append(flowers[tree[i][1]-1]+cutFlowers(tree[0:i]+tree[i+1:len(tree)],flowers,k-1))
    return min(res)
n=int(input())
flowers=list(map(int,input().split()))
tree=[]
beauty=sum(flowers)
for i in range(n-1):
    tree.append(list(map(int,input().split())))
for i in range(n-1):
    if tree[i][0]==1:
        restruct(tree,i)
res=[]
for i in range(n):
    res.append(beauty-cutFlowers(tree,flowers,i))
print(max(res),end="")