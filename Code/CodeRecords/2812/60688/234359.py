num=int(input());
listnums=input().split(" ");
listnums.sort();
mtset=set(listnums);
result=0;
if(listnums[0]=='0'):
    result=len(mtset)-1;
else:
    result=len(mtset);
print(result)