strnum=input();
numlist=[];
for i in strnum:
    numlist.append(int(i));
maxtimes=max(numlist);
resultnums=[];
for i in range(maxtimes):
    thisresult=[0]*len(numlist);
    for j in range(len(numlist)):
        if(numlist[j]!=0):
            thisresult[j]=1;
            numlist[j]=numlist[j]-1;
    resultnums.append(thisresult);
results=[];
for i in resultnums:
    i=list(i);
    i.reverse();
    base=1;
    tempresult=0;
    for j in range(len(numlist)):
        tempresult+=i[j]*base;
        base*=10;
    results.append(str(tempresult));
resultstr=" ".join(results);
print(len(results))
print(resultstr)