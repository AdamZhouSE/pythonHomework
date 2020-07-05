def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def rockGame(list):
    countA=0;
    countB=0;
    i=0;
    while(list!=[]):
        if(list[0]>=list[len(list)-1]):
            if(i%2==0):
                countA+=list[0];
            else:
                countB+=list[0];
            list.remove(list[0]);
        else:
            if(i%2==0):
                countA+=list[len(list)-1];
            else:
                countB+=list[len(list)-1];
            list.remove(list[len(list)-1]);
        i+=1;
    if(countA>countB):
        print(True);
    else:
        print(False);

list=makeIntList(str(input()).split(","));
rockGame(list);