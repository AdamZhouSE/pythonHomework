times=int(input());
numblist=input().split(" ");
numblist.sort();
afterset=set(numblist);
result=0;
if(numblist[0]=='0'):
    result=len(afterset)-1;
else:
    result=len(afterset);
print(result)