def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def grumpyBoss(cusList,grumList,X):
    i=0;
    ans=0;
    tempCus=[];
    while(i<len(cusList)):
        tempCus.append(cusList[i]);
        i+=1;

    i=0;
    while(i<len(cusList)-(X-1)):
        cusList = [];
        j=0;
        while (j < len(tempCus)):
            cusList.append(tempCus[j]);
            j += 1;
        SUM = 0;
        tempList=cusList[i:i+X];
        SUM+=sum(tempList);
        var=0;
        while(var<X):
            cusList[i+var]=-1;
            var+=1;
        x=0;
        while(x<len(cusList)):
            if(cusList[x]!=-1):
                if(grumList[x]==0):
                    SUM+=cusList[x];
            x+=1;
        if(SUM>ans):
            ans=SUM;
        i+=1;
    print(ans);




cusList=makeIntList(input().split(","));
grumList=makeIntList(input().split(","));
X=int(input());
grumpyBoss(cusList,grumList,X);
