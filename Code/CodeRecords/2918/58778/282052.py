n=int(input())
boxlist=list(map(int,input().split( )))
piles=[]
boxlist.sort()
i=0
#tomakeonepile
for z in range(n):
    temp=[]
    for i in range(len(boxlist)):
        if(len(temp)==0):
            temp.append(boxlist[i])
        else:
            if(len(temp)<=boxlist[i]):
                temp.append(boxlist[i])
    for j in temp:
        del boxlist[boxlist.index(j)]
    if(len(temp)!=0):
        piles.append(temp)
print(len(piles))