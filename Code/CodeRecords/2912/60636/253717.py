source=list(input())
res=[]
for i in range(1,len(source)+1):
    for j in range(len(source)-i+1):
        alls=[]
        for a in source[j:j+i]:
            if(not a in alls):
                alls.append(a)
        if(len(alls)==i):
            res.append(i)
            break
print(max(res))
        