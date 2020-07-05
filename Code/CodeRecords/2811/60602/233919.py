def DZYhashmap(Total,numList):
    count=0;
    emptyList = [];
    while (count < int(Total[0])):
        emptyList.append("a");
        count += 1;
    count=0;
    while(count<len(numList)):
        if(emptyList[int(numList[count])%int(Total[0])]=="a"):
            emptyList[int(numList[count])%int(Total[0])]=numList[count];
        else:
            return count+1;
        count+=1;
    return -1;

Total=str(input());
Total=Total.split(" ");
count=0;
numList=[];
while(count<int(Total[1])):
    numList.append(int(input()));
    count+=1;
print(DZYhashmap(Total,numList));