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
def mostStable(list):
    if(len(list)<=2):
        print(0);
    else:
        delleast=quickSort(list);
        delleast.remove(delleast[0]);
        DLcount=int(delleast[len(delleast)-1])-int(delleast[0]);
        delmost=quickSort(list);
        delmost.remove(delmost[len(delmost)-1]);
        DMcount=int(delmost[len(delmost)-1])-int(delmost[0]);
        print(min(DLcount,DMcount));
Total=int(input());
i=0;
list=[];
# while(i<Total):
#
#     i+=1;
list=str(input());
list=list.split(" ");
mostStable(list);