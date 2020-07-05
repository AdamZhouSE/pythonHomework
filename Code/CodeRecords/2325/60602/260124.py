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
def cardIntoGroup(list):
    list=quickSort(list);
    ans=[];
    i=0;
    count=1;
    while(i<len(list)-1):
        if(list[i+1]==list[i]):
            count+=1;
        else:
            ans.append(count);
            count=1;
        i+=1;
    ans.append(count);
    test=min(ans);
    if(test<2):
        print(False);
        return
    else:
        i=0;
        judge=True;
        while(i<len(ans)):
            if(ans[i]%test!=0):
                judge=False;
            i+=1;
        print(judge);


list=str(input());
list=makeIntList(list.split(","));
cardIntoGroup(list);