def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def forbidSkip(list):
    i=0;
    count=0;
    while(i<len(list)):
        if(list.index(max(list))==0):
            if(list[list.index(max(list))+1]!=0):
                list[list.index(max(list))]=0;
            else:
                count+= list[list.index(max(list))];
                list[list.index(max(list))]=-1;
        elif(list.index(max(list))==len(list)-1):
            if(list[list.index(max(list))-1]!=0):
                list[list.index(max(list))]=0;
            else:
                count+= list[list.index(max(list))];
                list[list.index(max(list))]=-1;
        else:
            if(list[list.index(max(list))-1]!=0 and list[list.index(max(list))+1]!=0):
                list[list.index(max(list))]=0;
            else:
                count+= list[list.index(max(list))];
                list[list.index(max(list))]=-1;
        i+=1;
    i=0;
    while(i<len(list)):
        if(list[i]!=-1):
            count+=list[i];
        i+=1;
    print(count);
Total=int(input());
i=0;
while(i<Total):
    size=int(input());
    list=makeIntList(input().split(" "));
    forbidSkip(list);
    i+=1;