rowstr=input();
strlist=list(rowstr);
strlistcopy=strlist.copy();
k=int(input());
standardlist=list(set(rowstr));
standardlist.sort();
# print(standardlist);
nowmin="";
times=0;
while(True):
    if(strlist==strlistcopy and times!=0):break;
    elem=strlist.pop(strlist.index(max(strlist[0:k])));
    strlist.append(elem);
    nowstr="".join(strlist);
    if(nowstr<rowstr):
        nowmin=nowstr;
    tempsetlist=list(set(strlist));
    tempsetlist.sort(key=strlist.index);
    if(tempsetlist==standardlist):
        break;
    times+=1;
print(nowmin)