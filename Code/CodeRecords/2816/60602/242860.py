def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def numberOnBoard(list):
    list=makeIntList(list);
    i=0;
    while(len(list)>1):
        if(i%2==0):
            list.remove(max(list));
        else:
            list.remove(min(list));
        i+=1;
    print(list[0]);

Total=int(input());
list=str(input());
list=list.split(" ");
numberOnBoard(list);