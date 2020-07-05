def Olym(list):
    i=0;
    testList=[0];
    while(i<len(list)):
        if(int(list[i])!=0):
            j=0;
            sum=0;
            while(j<len(testList)):
                if(testList[j]==list[i]):
                    break;
                else:
                    sum+=1;
                j+=1;
            if(sum==len(testList)):
                testList.append(list[i]);
        sum=0;
        i+=1;
    print(len(testList)-1);

Total=int(input());
list=str(input());
list=list.split(" ");
Olym(list);