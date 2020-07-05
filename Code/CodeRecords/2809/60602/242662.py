def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def makeTree(list):
    list=makeIntList(list);
    i=0;
    Big=0;
    Small=0;
    while(len(list)!=0):
        Big+=max(list);
        list.remove(max(list));
        if(len(list)!=0):
            Small+=min(list);
            list.remove(min(list));
    print(Big*Big+Small*Small);

    return

Total=int(input());
i=0;
list=str(input());
list=list.split(" ");
makeTree(list);