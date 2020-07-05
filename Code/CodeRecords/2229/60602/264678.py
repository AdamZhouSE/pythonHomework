def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def reverseCalcu(list):
    i=0;
    countGlo=0;
    countLoc=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[i]>list[j]):
               countGlo+=1;
            j+=1;
        i+=1;
    i=0;
    while(len(list)!=0 and i<len(list)-1):
        if(list[i]>list[i+1]):
            countLoc+=1;
        i+=1;
    if(countGlo==countLoc):
        print(True);
    else:
        print(False);


list=str(input());
list=makeIntList(list.split(","));
reverseCalcu(list);