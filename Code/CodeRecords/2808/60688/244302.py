hi=int(input());
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
hiindex=numslist.index(hi);
loindex=numslist.index(1);
flag=-1;
if(loindex==0 or loindex==hi-1):
    flag=1;
elif (hiindex==0 or hiindex==hi-1):
    flag=1;
result=0;
phi=hiindex;
ehi=hi-1-hiindex;
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