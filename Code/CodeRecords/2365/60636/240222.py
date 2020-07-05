number=int(input())
lists=[]
for i in range(number):
    source=[]
    num=int(input())
    lis=input().split(" ")
    for i in range(num):
        source.append(int(lis[i]))
    lists.append(source)
for i in range(len(lists)):
    parts=[]
    for x in lists[i]:
        parts.append(list(str(x)))
    result=""
    while(len(parts)!=0):
        
        max_0=0
        location=[]
        for x in range(len(parts)):
            if(int(parts[x][0])>max_0):
                max_0=int(parts[x][0])
        for x in range(len(parts)):
            if(int(parts[x][0])==max_0):
                location.append(x)
        possiable=[]
        for y in range(len(location)):
            possiable.append(parts[location[y]])
        if(len(possiable)==1):
            result=result+str(possiable[0][0])
            parts.pop(location[0])
        print(possiable)
    print(result)
        
        
        