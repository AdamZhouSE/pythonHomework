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
            nums=""
            for a in possiable[0]:
                nums=nums+a
            result=result+str(nums)
            parts.pop(location[0])
        else:
            length=[]
            for i in range(len(possiable)):
                length.append(len(possiable[i]))
            if(length.count(length[0])==len(length)):
                possiable_num=[]
                for z in possiable:
                    nums=""
                    for a in z:
                        nums=nums+a
                    possiable_num.append(int(nums))
                print(possiable_num)
                result=result+str(max(possiable_num))
                print(result)
                parts.pop(location[possiable_num.index(max(possiable_num))])
                print(parts)
            else:
                min_length=min(length)
                location_0=[]
                if(min_length==1):
                    for z in range(len(possiable)):
                        if(len(possiable[z])!=1):
                            if(int(possiable[z][1])<max_0):
                                possiable.pop(z)
                                length.pop(z)
                        else:
                            location_0=possiable[z]
                    if(len(possiable)==1):
                        result=result+str(possiable[0][0])
                        parts.pop(parts.index(possiable[0]))
                    else:
                        possiable.pop(possiable.index(location_0))
                        length.pop(possiable.index(location_0))
                        i=1
                        while(len(possiable)!=1):
                            if(length.count(length[0])==len(length)):
                                possiable_num=[]
                                for z in possiable:
                                    nums=""
                                    for a in z:
                                        nums=nums+a
                                    possiable_num.append(int(nums))
                                result=result+str(max(possiable_num))
                                parts.pop(location[possiable_num.index(max(possiable_num))])
                            else:
                                for a in range(len(possiable)):
                                    if(len(possiable[a])>i+1):
                                        if(int(possiable[a][i+1])<max_0):
                                            possiable.pop(a)
                                            length.pop(a)
                                if(len(possiable)==1):
                                    result=result+str(possiable[0][0])
                                    parts.pop(parts.index(possiable[0]))
                                else:
                                    max_1=int(possiable[0][i])
                                    for a in range(len(possiable)):
                                        if(max_1<int(possiable[a][i])):
                                            max_1=int(possiable[a][i])
                                    for a in range(len(possiable)):
                                        if(int(possiable[a][i])<max_1):
                                            possiable.pop(a)
                                            length.pop(a)
                                    if(len(possiable)==1):
                                        result=result+str(possiable[0][0])
                                        parts.pop(parts.index(possiable[0]))
                                    else:
                                        i=i+1
        print(possiable)
    print(result)
        
        
        