n=int(input());
timeList = [int(x) for x in input().split()];
timeList.sort();
num = 0;
for i in range(0,n):
    for i in range(0,len(timeList)):
        if(timeList[i]<sum(timeList[:i])):
            timeList.remove(timeList[i]);
            break;

print(len(timeList));