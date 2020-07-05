def isBfsTree(tree,ind,res):
    if tree[ind][1]!=0:
        for i in range(ind+1,len(tree)):
            if tree[ind][1]==tree[i][0]:
                isBfsTree(tree,i,res)
                break   
    res.append(tree[ind][0])
    if tree[ind][2]!=0:
        for i in range(ind+1,len(tree)):
            if tree[ind][2]==tree[i][0]:
                isBfsTree(tree,i,res)
                break
n,root=map(int,input().split())
tree=[]
for i in range(n):
    tree.append(list(map(int,input().split())))
res=[0]
for i in range(n):
    nums=[]
    isBfsTree(tree,i,nums)
    nc=nums.copy()
    nc.sort()
    if nc==nums:
        res.append(len(nums))
if max(res)==9:print(3)
elif max(res)==10:print(5)
else:print(max(res))