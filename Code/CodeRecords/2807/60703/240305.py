n,m = map(int,input().split());
BOXnum = [int(x) for x in input().split()];
KEYnum = [int(x) for x in input().split()];
oddOfBox = 0;
oddOfKey = 0;
doubleOfBox = 0;
doubleOfKey = 0;
for i in BOXnum:
    if(i%2==1):
        oddOfBox+=1;
    else:
        doubleOfBox+=1;
for i in KEYnum:
    if(i%2==1):
        oddOfKey+=1;
    else:
        doubleOfKey+=1;
res = 0;
if(oddOfKey>doubleOfBox):
    res+=doubleOfBox;
else:
    res+=oddOfKey;

if(oddOfBox>doubleOfKey):
    res+=doubleOfKey;
else:
    res+=oddOfBox;
print(res);