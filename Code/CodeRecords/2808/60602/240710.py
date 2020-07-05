def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;

def exchangeElement(list):
    list=makeIntList(list);
    Max=max(list);
    Min=min(list);
    i=list.index(Max);
    j=list.index(Min);
    tempMax=max(i,len(list)-1-i);
    tempMin=max(j,len(list)-1-j);
    print(max(tempMax,tempMin));
Total=int(input());
list=str(input());
list=list.split(" ");
exchangeElement(list);