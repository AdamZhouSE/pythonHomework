nums=int(input());
numslist=(input().split(" "));
numslist=list(int(x) for x in numslist);
numslist.sort();
numset=set(numslist);
numset=list(numset);
result=0;
if(len(numset)>3):
    result=-1;
elif len(numset)==3:
    flag=set[1]==((set[0]+set[2])/2);
    if flag:
        result=set[2]-((set[0]+set[2])/2);
    else:result=-1;
elif len(numset)==3:
    result=set[1]-set[0];
else: result=0;
print(result)