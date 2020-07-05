n = int(input());
numList = [int(x) for x in input().split()];
biggest = 1;
index  =1;
lenList = [];
while(index!=len(numList)):
    if(numList[index-1]<numList[index]):
        index+=1;
    else:
        lenList.append(index);
        numList = numList[index:];
        index  = 1;
if(index==len(numList)):
    lenList.append(index);
lenList.sort(reverse=True);
print(lenList[0]);