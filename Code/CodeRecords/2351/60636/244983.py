n=int(input())
sources=[]
for i in range(n-1):
    x=input().split(" ")
    source=[]
    for a in x:
        source.append(int(a))
    sources.append(source)
number=[]
for i in range(1,n+1):
    delete=sources.copy()
    for y in sources:
        if(i in y):
            delete.pop(delete.index(y))
    all_length=[]
    while(len(delete)!=0):
        all=[]
        all.append(delete[0][0])
        all.append(delete[0][1])
        delete.pop(0)
        if(len(delete)==1):
            all_length.append(1)
            break
        else:
            save=delete.copy()
            for i in delete:
                if((i[0] in all)|(i[1] in all)):
                    if(not i[0] in all):
                        all.append(i[0])
                    elif(not i[1] in all):
                        all.append(i[1])
                    save.pop(save.index(i))
            delete=save
            all_length.append(len(all))
    number.append(max(all_length))
res=[]
for i in range(len(number)):
    if(number[i]==min(number)):
        res.append(i+1)
print(*res)