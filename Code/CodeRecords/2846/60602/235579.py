def nameList(list):
    i=0;
    j=0;
    count=0;
    judge=False;
    while(i<len(list)):
        if (int(list[i]) == 0):
            i+=1;
            continue;
        while(j<len(list)):
            if(int(list[j])==0):
                j+=1;
                continue;
            if(list[j]==list[i] and j!=i):
                judge=True;
                break;
            j+=1;
        j=0;
        if(not judge):
            count+=1;
        judge=False;
        i+=1;
    if(count==0):
        sum=0;
        for element in list:
            if(int(element)==0):
                sum+=1;
        if(sum!=len(list)):
            count=1;
    print(count);

Total=int(input());
sum=0;
i=0;
# list=[];
# while(i<Total):
#     temp = str(input());
#     list.append(temp);
#     i+=1;
listSum=str(input());
listSum=listSum.split(" ");
# for element in listSum:
#     sum+=int(element);
nameList(listSum);