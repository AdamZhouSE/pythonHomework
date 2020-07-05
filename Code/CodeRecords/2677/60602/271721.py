def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def howManyXor(list):
    i=0;
    count=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            if(list[i]==list[j]):
                count+=1;
            j+=1;
        i+=1;
    print(count);
Total=int(input());
i=0;
while(i<Total):
    temp=int(input());
    list=makeIntList(input().split(" "));
    howManyXor(list);
    i+=1;