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
        max=0
        location=[]
        for x in range(len(parts)):
            if(int(parts[x][0])>max):
                max=int(parts[x][0])
        for x in range(len(parts)):
            if(int(parts[x][0])==max):
                location.append(x)
        length=[]
        for y in range(len(location)):
            length.append(len(parts[x]))
        if(length.count(min(length))==1):
            result=result+str(*parts[location[length.index(min(length))]])
            print(result)
            parts.pop(lists[i].index(lists[i][location[length.index(min(length))]]))
            print(parts)
        else:
            nums=[]
            for a in location:
                if(len(parts[a])==min(length)):
                    nums.append(lists[i][a])
            print(nums)
            print(parts)
            result=result+str(max(nums))
            lists[i].pop(lists[i].index(max(nums)))
    print(result)
        
        