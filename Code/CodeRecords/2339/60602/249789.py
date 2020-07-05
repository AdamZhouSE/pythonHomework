def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
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
def reverseTime(list):
    list=makeIntList(list);
    i=0;
    count=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[i]>list[j]):
                count+=1;
            j+=1;
        i+=1;
    print(count);

Total=int(input());
while(Total>0):
    temp=int(input());
    list=str(input());
    list=list.split(" ");
    reverseTime(list);
    Total-=1;
