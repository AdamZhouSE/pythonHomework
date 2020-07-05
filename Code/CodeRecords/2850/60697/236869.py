num=int(input())
sizes=list(map(int,input().split(' ')))
count=0
maxsize=0
res=0
for i in range(num):
    res=0
    for j in range(i,num):
        if(sizes[j]==0):
            res=res+1
        else:
            res=res-1
        maxsize=max(maxsize,res)
for i in range(num):
    if(sizes[i]==1):
        maxsize=maxsize+1
print(maxsize)