def quickSort(list):
    if(len(list)>1):
        count=1;
        x=list[0];
        leftList=[];
        rightList=[];
        while(count<len(list)):
            if(int(list[count])>=int(x)):
                rightList.append(list[count]);
            else:
                leftList.append(list[count]);
            count+=1;
        leftList.append(x);
        return quickSort(leftList)+quickSort(rightList);
    else:
        return list;
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def rabbitHouse(list):
    list=quickSort(list);
    i=0;
    count=list[0]+1;
    while(i<len(list)-1):
        if(list[i]!=list[i+1]):
            count+=list[i+1]+1;
        i+=1;
    print(count);

list=str(input());
list=makeIntList(list.split(","));
rabbitHouse(list);