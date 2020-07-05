def makeIntList(list):
    count=0;
    while(count<len(list)):
        list[count]=int(list[count]);
        count+=1;
    return list;
def compareSearch(listA,listB):
    ans=[];
    count=0;
    listA=makeIntList(listA);
    listB=makeIntList(listB);
    for i in listB:
        for j in listA:
           if(j<=i):
                count+=1;
        ans.append(count);
        count=0;
    temp=0;
    while(temp<len(ans)-1):
        print(ans[temp],end=" ");
        temp+=1;
    print(ans[len(ans)-1]);


Total=str(input());
listA=str(input());
listA=listA.split(" ");
listB=str(input());
listB=listB.split(" ");
compareSearch(listA,listB);