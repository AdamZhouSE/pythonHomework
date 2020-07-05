def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def Bigger(list,d):
    i=1;
    count=0;
    list=makeIntList(list);
    while (i<len(list)):
        if(list[i]<=list[i-1]):
            list[i]+=d;
            count+=1;
            i-=1;
        i+=1;
    print(count);

Total=str(input());
Total=Total.split(" ");
list=str(input());
list=list.split(" ");
Bigger(list,int(Total[1]));