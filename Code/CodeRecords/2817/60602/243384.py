def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def threeChild(list):
    list=makeIntList(list);
    i=0;
    while(i<len(list)):
        list[i]-=1;
        i+=1;
    i=0;
    while(i<len(list)):
        if(list[list[list[i]]]==i):
            print("YES");
            return;
        i+=1;
    print("NO");

Total=int(input());
list=str(input());
list=list.split(" ");
threeChild(list);