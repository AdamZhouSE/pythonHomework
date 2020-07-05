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
def findNum(list):
    list=quickSort(makeIntList(list));
    i=0;
    j=0;
    ans=[];
    temp=0;
    judge=True;
    while(i<len(list)-1):
        if(list[i]!=i+j+1 and judge):
            temp=i+j+1;
            judge=False;
        if(list[i]==list[i+1]):
            ans.append(list[i]);
        i+=1;
    if(ans==[]):
        print(0,end=" ");
    else:
        print(min(ans),end=" ");
    if(temp==5):
        print(list);
    print(temp);

Total=int(input());
while(Total>0):
    temp=int(input());
    list=str(input());
    list=list.split(" ");
    findNum(list);
    Total-=1;