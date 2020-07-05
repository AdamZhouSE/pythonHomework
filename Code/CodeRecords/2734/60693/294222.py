def isPickable(flowerindex:{},color:int,l,r):
    if len(flowerindex[color])==1:
        return False
    times=0
    for i in flowerindex[color]:
        if i in range(l-1,r):
            times+=1
            if times>1:
                return True
    return False

from collections import defaultdict
ncm=list(map(int,input().split()))
n,c,m=ncm[0],ncm[1],ncm[2]
flowers=list(map(int,input().split()))
flower_index=defaultdict(list)
for idx,color in enumerate(flowers):
    flower_index[color].append(idx)
# print(flower_index)
for _ in range(m):
    path=input().split()
    l,r=int(path[0]),int(path[1])
    res=[]
    for i in range(l-1,r):
        if isPickable(flower_index,flowers[i],l,r) and flowers[i] not in res:
            res.append(flowers[i])
    print(len(res))