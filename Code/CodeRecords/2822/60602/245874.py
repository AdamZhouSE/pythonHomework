def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def soldierCards(listA,listB):
    roundNum=0;
    listA=makeIntList(listA);
    listB=makeIntList(listB);
    tempA=[];
    for element in listA:
        tempA.append(element);
    while(listA!=[] and listB!=[]):
        roundNum+=1;
        if(listA[0]>listB[0]):
            listA.append(listB[0]);
            listA.append(listA[0]);
            listA.remove(listA[0]);
            listB.remove(listB[0]);
        else:
            listB.append(listA[0]);
            listB.append(listB[0]);
            listB.remove(listB[0]);
            listA.remove(listA[0]);
        if(tempA==listA):
            print(-1);
            return
    print(roundNum,end=" ");
    if(listA==[]):
        print(2);
    else:
        print(1);


Total=int(input());
listA=str(input());
listA=listA.split(" ");
listB=str(input());
listB=listB.split(" ");
listA=listA[1:];
listB=listB[1:];

soldierCards(listA,listB);