rowstr=input();
rowlist=rowstr.split(" ");
cilist=input().split(" ");
cilist=list(int(x) for x in cilist);
cilist.sort();           #！！！不能串式编程！！！sort不返回任何值！！！
corsnum=int(rowlist[0]);
init=int(rowlist[1]);
timecostlist=[];
timelist=[];
if(init>corsnum):
    for i in range(init+1):
        timecostlist.append(i);
    timecostlist.sort();
    timecostlist.reverse();
    timelist=timecostlist[0:init-1];
else:
    for i in range(1,init+1):
        timecostlist.append(i);
    for j in range(corsnum-init):
        timecostlist.append(1);
    timecostlist.sort();
    timecostlist.reverse();
    timelist=timecostlist;
result=0;
for i in range(corsnum):
    temp=int(cilist[i]);
    result=result+timelist[i]*temp;
print(result)