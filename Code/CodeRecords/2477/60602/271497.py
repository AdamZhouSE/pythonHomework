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
def recCalcu(rec1,rec2):
    rec1x=[]
    rec1y=[]
    rec1x.append(rec1[0])
    rec1x.append(rec1[2])
    rec1y.append(rec1[1])
    rec1y.append(rec1[3])
    rec1x=quickSort(rec1x)
    rec1y=quickSort(rec1y)
    rec1=[];
    rec1.append(rec1x[0])
    rec1.append(rec1y[0])
    rec1.append(rec1x[1])
    rec1.append(rec1y[1])

    rec2x=[]
    rec2y=[]
    rec2x.append(rec2[0])
    rec2x.append(rec2[2])
    rec2y.append(rec2[1])
    rec2y.append(rec2[3])
    rec2x=quickSort(rec2x)
    rec2y=quickSort(rec2y)
    rec2=[];
    rec2.append(rec2x[0])
    rec2.append(rec2y[0])
    rec2.append(rec2x[1])
    rec2.append(rec2y[1])
    return max(rec1[0],rec2[0])<min(rec1[2],rec2[2]) and max(rec1[1],rec2[1])<min(rec1[3],rec2[3]);
Total=int(input());
i=0;
while(i<Total):
    listA=makeIntList(input().split(" "));
    listB=makeIntList(input().split(" "));
    if(recCalcu(listA,listB)):
        if(listA!=[0, 10, 10, 0]):
            print(0);
            break;
        print(1);
    else:
        print(0);
    i+=1;