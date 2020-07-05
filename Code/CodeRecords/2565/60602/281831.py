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
listA=makeIntList(input().split(","));
listB=makeIntList(input().split(","));
list=quickSort(listA+listB);
if(len(list)%2!=0):
    print(float(list[len(list)//2]));
else:
    print(format((float(list[len(list) // 2-1])+float(list[len(list)//2]))/2,'.5f'));


