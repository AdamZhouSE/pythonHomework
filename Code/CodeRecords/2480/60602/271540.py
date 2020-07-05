def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def departNum(list):
    i=0;
    temp=[];
    while(i<len(list)):
        if(list[i]%2==0):
            temp.append(list[i]);
            list.remove(list[i]);
            i-=1;
        i+=1;
    list=temp+list;
    i=0;
    while(i<len(list)-1):
        print(list[i],end=" ");
        i+=1;
    print(list[len(list)-1],end=" ");
    print();
Total=int(input());
i=0;
while(i<Total):
    temp=int(input());
    list=makeIntList(input().split(" "));
    departNum(list);
    i+=1;
