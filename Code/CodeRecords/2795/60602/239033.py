def makeIntList(list):
    count=0;
    while(count<len(list)):
        list[count]=int(list[count]);
        count+=1;
    return list;
def leastD(list):
    list=makeIntList(list);
    Min=min(list);
    Max=max(list);
    equalNum=Min;
    D=0;
    range=Max-Min;
    ans=[];

    while(equalNum<=Max):
        temp=equalNum;
        count=0;
        judge=True;
        for element in list:
            if(element+D==equalNum or element-D==equalNum or element==equalNum):
                count+=1;
            else:
                D+=1;
                judge=False;
                break;
        if(count==len(list)):
            ans.append(D);
        if(not judge):
            equalNum-=1;
        equalNum+=1;
        if(D>range):
            equalNum+=1;
        if(temp!=equalNum):
            D=0;
    if(len(ans)!=0):
        print(min(ans));
    else:
        print(-1);

Total=int(input());
list=str(input());
list=list.split(" ");
leastD(list);