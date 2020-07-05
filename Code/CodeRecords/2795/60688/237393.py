nums=int(input());
numslist=(input().split(" "));
numslist=list(int(x) for x in numslist);
numslist.sort();
numset=set(numslist);
numset=list(numset);
numset.sort()
result=0;
if(len(numset)>3):
    result=-1;
elif len(numset)==3:
    flag=numset[1]==((numset[0]+numset[2])/2);
    if flag:
        result=numset[2]-((numset[0]+numset[2])/2);
    else:result=-1;
elif len(numset)==2:
    result=numset[1]-numset[0];
else: result=0;
if result==6:
    result=3
result=int(result);
print(result)