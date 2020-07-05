num=int(input())
for i in range(num):
    length=int(input())
    words=input().split()
    groups=[[words[0]]]
    for j in range(1,length):
        couldFind=False
        for l in groups:
            temp=l[0]
            judge=True
            for k in words[j]:
                if k in temp:
                    temp=temp[0:temp.index(k)]+temp[temp.index(k)+1:]
                else:
                    judge=False
                    break
            if temp!="":
                judge=False
            if judge:
                l.append(words[j])
                couldFind=True
        if not couldFind:
            groups.append([words[j]])
    groups.sort(key=lambda x:len(x))
    result=str(len(groups[0]))
    for i in range(1,len(groups)):
        result+=" "+str(len(groups[i]))
    print(result)