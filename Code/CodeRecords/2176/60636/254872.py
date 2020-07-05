source=list(input())
alls=[]
for i in source:
    if(not i in alls):
        alls.append(i)
alls.sort()
res=[]
for i in alls:
    for j in range(len(source)-1,-1,-1):
        if(source[j]==i):
            res.append(j)
print(*res)