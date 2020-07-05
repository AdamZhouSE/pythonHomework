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
Total=int(input());
i=0;
list=[];
# while(i<Total):
#
#     i+=1;
list=str(input());
list=list.split(" ");
list=quickSort(list);
while(len(list)!=1):
    print(list[0],end=" ");
    list.remove(list[0]);
print(list[0]);