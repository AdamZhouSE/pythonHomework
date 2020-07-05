times=int(input());
rainfalls=[];
for i in range(times):
     thisttime=int(input());
     rain=input().split(" ");
     rain=list(int(x) for x in rain);
     rainfalls.append(rain);
# print(rainfalls)
#首先搞定单个然后搞定所有！！
#开始构建循环
allrainfalls=[];
for i in range(len(rainfalls)):
    thisrainfall=rainfalls[i];
    begin=1;
    end=len(thisrainfall);
    thisrainfall.append(0);
    thisrainfall.insert(0,0);
    i=1;
    allrains=0;
    while(i<end):#-1
        thisrain=thisrainfall[i];
        if thisrain!=max(thisrainfall[i-1:i+2]):
            i+=1;
            continue;
        else:
            j=i+1;
            while(j <=end):
                endp=thisrainfall[j];
                if endp != max(thisrainfall[j - 1:j + 2]):
                    j += 1;
                    continue;
                else:break;

            standard=0;
            if endp<thisrain:standard=endp;
            else:standard=thisrain;

            while(i<j):
                i+=1;
                temp=standard-thisrainfall[i];
                if temp<=0:continue
                else:allrains+=temp;

    allrainfalls.append(allrains);
for i in allrainfalls:
    print(i);