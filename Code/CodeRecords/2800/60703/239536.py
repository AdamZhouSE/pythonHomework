n,d=map(int,input().split());
numList=[int(x) for x in input().split()];
length = len(numList);
num=0;
for i in range(0,length-1):
    numList[i];
    numList[i+1];
    while(not(numList[i]<numList[i+1])):
        numList[i+1]+=d;
        num+=1;

print(num);