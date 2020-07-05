def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def leaderNum(list):
    i=0;
    judge=True;
    ans=[];
    while(i<len(list)):
        j=i;
        while(j<len(list)):
            if(list[i]<list[j]):
                judge=False;
            j+=1;
        if(judge):
            ans.append(list[i]);
        judge=True;
        i+=1;
    x=0;
    while(x<len(ans)-1):
        print(ans[x],end=" ");
        x+=1;
    print(ans[len(ans)-1]);

Total=int(input());
i=0;
while(i<Total):
    N=int(input());
    list=makeIntList(input().split(" "));
    leaderNum(list);
    i+=1;
