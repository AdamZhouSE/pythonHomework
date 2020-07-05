n=int(input());
strList = input().split();
numList=[];
resLIST=[];
for i in strList:
    numList.append(int(i));
for i in range(0,len(numList)-1):
    if(numList[i+1]==1):
        resLIST.append(numList[i]);
resLIST.append(numList[len(numList)-1]);
res="";
for j in resLIST:
    res=res+str(j)+" ";
print(len(resLIST));
print(res[:len(res)-1]);