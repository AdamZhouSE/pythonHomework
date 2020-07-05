import re
rowstr=input();
rownums=re.split(r"\W",rowstr)
symbles=re.split(r"\w+",rowstr)
while("" in symbles):
    symbles.remove("");
for i in range(len(rownums)):
    if("x" in rownums[i] and len(rownums[i])!=1):
        rownums[i]=rownums[i][0:len(rownums[i])-1]+"*x";
finallstr="";
for i in range(len(symbles)):
    finallstr+=rownums[i]+symbles[i];
finallstr+=rownums[len(rownums)-1]

stringlist=finallstr.split("=");
l=stringlist[0]
r=stringlist[1]
#处理左侧：
x=0;
lnumexe=eval( l);
x=1
lxc=eval(l)-lnumexe;

x=0;
rnumexe=eval( r);
x=1
rxc=eval( r)-rnumexe;
result="";
if(lnumexe==rnumexe==0):
    if(lxc==rxc):
        result="Infinite solutions";
    else:result="x=0";
# elif(lxc==rxc):#可以放到计算中
#     if((lnumexe==0 and rnumexe!=0) or(rnumexe==0 and lnumexe!=0)):
#
else:
    if (lxc==rxc and (lnumexe==0 and rnumexe!=0) or(rnumexe==0 and lnumexe!=0)):
        result = "No solution";
    else:
        lxc-=rxc;
        rnumexe-=lnumexe;
        x=rnumexe//lxc;
        result="x="+str(x)
print(result)