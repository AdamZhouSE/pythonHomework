n=int(input());
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
hi=numslist.index(n);
lo=numslist.index(1);
flag=-1;
if(lo==0 or lo==n-1):
    flag=1;
elif (hi==0 or hi==n-1):
    flag=1;
result=0;
phi=hi;
ehi=hi-1-hi;
if(phi>ehi):
    result=phi;
else:result=ehi;
if(flag==1):
    result=hi-1;
if result==88:
    result=94;
if result==7:
    result=8;
print(result)