times=int(input());
rainfalls=[];
for i in range(times):
     thisttime=int(input());
     rain=input().split(" ");
     rain=list(int(x) for x in rain);
     rainfalls.append(rain);
print(rainfalls)
#首先搞定单个然后搞定所有！！
#开始构建循环
allrainfalls=[];
for i in range(len(rainfalls)):

    thisrainfall=rainfalls[i];
    i=0;
    allrains=0;
    while(i<len(thisrainfall)-1):#-1
        thisrain=thisrainfall[i];
        nextrain=thisrainfall[i+1];
        if thisrain<=nextrain:
            i+=1;
            continue;
        else:
            j=i+1;
            while (j < len(thisrainfall) and thisrainfall[j]< thisrainfall[i]): j+=1;
            j=j-1;
            while(i<j):
                i+=1;
                allrains+=thisrain-thisrainfall[i];
    allrainfalls.append(allrains);
for i in allrainfalls:
    print(i);