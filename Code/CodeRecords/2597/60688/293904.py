flowers={};
reqstr=input()
if(len(reqstr)==1):
    reqtype=int(reqstr)
else:
    reqlist = reqstr.split(" ");
    reqlist = list(int(x) for x in reqlist);
    reqtype=reqlist[0];
while(reqtype!=-1):
    if(reqtype==1):
        flowers[str(reqlist[2])]=reqlist[1];
    if (reqtype == 2):
        flowers[str(reqlist[2])] = reqlist[1];
        #找到最贵的key：
        keyslist=list(flowers.keys());
        keyslist.sort(reverse=True);
        thiskey=keyslist[0];
        del flowers[thiskey];
    if (reqtype == 3):
        flowers[str(reqlist[2])] = reqlist[1];
        #找到最贵的key：
        keyslist=list(flowers.keys());
        keyslist.sort(reverse=False);
        thiskey=keyslist[0];
        del flowers[thiskey];
    reqstr = input()
    if (len(reqstr) == 1):
        reqtype = int(reqstr)
    else:
        reqlist = reqstr.split(" ");
        reqlist = list(int(x) for x in reqlist);
        reqtype = reqlist[0];
cs=list(flowers.keys())
cs = list(int(x) for x in cs);
cresult=sum(cs)
ws=list(flowers.values())
wsresult=sum(ws)
print(str(wsresult)+" "+str(cresult),end="")