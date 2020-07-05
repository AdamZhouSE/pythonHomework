def quickSort(list):
    if(len(list)>1):
        count=1;
        x=list[0];
        leftList=[];
        rightList=[];
        while(count<len(list)):
            if(list[count]>=x):
                rightList.append(list[count]);
            else:
                leftList.append(list[count]);
            count+=1;
        leftList.append(x);
        return quickSort(leftList)+quickSort(rightList);
    else:
        return list;
Total=int(input());
i=0;
list=[];
while(i<Total):
    temp=str(input());
    temp=temp.split(" ");
    sum=0;
    for element in temp:
        sum+=int(element);
    list.append(sum);
    i+=1;
# list=str(input());
# list=list.split(" ");
SmithScore=list[0];
list=quickSort(list);
list.reverse();
print(list.index(SmithScore)+1);