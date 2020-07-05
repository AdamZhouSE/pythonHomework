def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def soldiersMedal(list,count):
    judge=True;
    i=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[i]==list[j]):
                list[j]+=1;
                count+=1;
                judge=False;
            j+=1;
        i+=1;
    if(judge):
        return count;
    else:
        return soldiersMedal(list,count);



Total=int(input());
list=str(input());
list=makeIntList(list.split(" "));
print(soldiersMedal(list,0));