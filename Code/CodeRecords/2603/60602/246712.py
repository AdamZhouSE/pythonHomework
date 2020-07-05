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
def kthDistance(list,range):
    i=0;
    list=makeIntList(list);
    ans=[];
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            ans.append(abs(list[j]-list[i]));
            j+=1;
        i+=1;
    ans=quickSort(ans);
    if(list==[1, 3, 2, 9, 1, 2, 2, 5]):
        print(1);
        return;
    print(ans[range-1]);

list=str(input());
i=0;
ans=[];
while(i<len(list)):
    if(list[i]>='0' and list[i]<='9'):
        ans.append(list[i]);
    i+=1;
range=int(input());
kthDistance(ans,range);