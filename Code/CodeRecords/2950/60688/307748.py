string=input()
strlist=list(string)
strlist=list(int(a) for a in strlist)
ist=True
res=0
id2=0
id5=0
temp=list()
while(True):
    if(sum(strlist)==0):
        break
    if(2 in strlist[id5:]):
        id2=strlist[id5:].index(2)+id5
        temp.append(id2)
        if(5 in strlist[id2:]):
            id5=strlist[id2:].index(5)+id2
            temp.append(id5)
        else:
            ist=False
            break
    else:
        if(len(temp)==0 and 5 in strlist):
            ist=False
            break
        for b in range(0,len(temp)):
            strlist[temp[b]]=0
        temp.clear()
        res=res+1
        id2=0
        id5=0
if(ist): print(res)
else: print(-1)
