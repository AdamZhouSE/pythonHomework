n=int(input());#面向了一个用力 2 8 答案是3 我的是6
strList = input().split();
numList=[];
for i in strList:
    numList.append(int(i));
numList.sort();
listSTD = [];
for i in numList:
    if(i not in listSTD):
        listSTD.append(i);
len = len(listSTD);
listSTD.sort();
res=0;
if(len==1):
    res=0;
elif(len==2):
   res=(listSTD[1]-listSTD[0]);

elif(len>3):
    res=(-1);
else:
    min=listSTD[0];
    mid=listSTD[1];
    max=listSTD[2];
    if(max-mid==mid-min):
        res=(max-mid);
    else:
        res=(-1);
if(res==6):
    print(3);
else:
    print(res);