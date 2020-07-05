from collections import Counter
n=int(input())
l=[]
def getk(i,j):
    return float('Inf') if i[1]-j[1]==0 else (i[0]-j[0])/(i[1]-j[1])
for i in range(n):
    l.append(list(map(int,input().split(","))))
ans=0
for i in l:
    samepoint=0
    for j in l:
        if j==i:
            samepoint+=1
    count=Counter(getk(i,j) for j in l if j!=i)
    tmpmax=count.most_common(1)[0][1]+samepoint if count else samepoint
    ans=max(tmpmax,ans)
print(ans)