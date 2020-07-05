nums=int(input());
result=0;
numlist=input().split(" ");
numlist=list(int(x) for x in numlist);
numlist.sort();
cha1=numlist[len(numlist)-1]-numlist[1];
cha2=numlist[len(numlist)-2]-numlist[0];
if cha1>cha2:
    result=cha2;
else:result=cha1;
if(nums==2):
    result=0;
print(result);