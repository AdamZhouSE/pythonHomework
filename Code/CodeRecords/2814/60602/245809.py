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
def SusiShopping(list):
    list=makeIntList(list);
    list=quickSort(list);
    ans=1;
    sum=min(list);
    list.remove(min(list));
    while(True):
        i=0;
        temp=[];
        while(i<len(list)):
            if(list[i]>=sum):
                temp.append(list[i]);
            i+=1;
        if(temp!=[]):
            sum+=min(temp);
            list.remove(min(temp));
            ans+=1;
        else:
            print(ans);
            return
    
Total=int(input());
list=str(input());
list=list.split(" ");
SusiShopping(list);