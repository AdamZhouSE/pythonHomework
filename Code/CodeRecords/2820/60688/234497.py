timelist=[1]*24;
clintnum=int(input());
hourbuffer=-1;
miubuffer=-1;
for i in range(clintnum):
    rowline=input().split(" ");
    hi=int(rowline[0]);
    mi=int(rowline[1]);
    if(hi==hourbuffer and mi==miubuffer):
        timelist[hi]=timelist[hi]+1;
        hourbuffer=hi;
        miubuffer=mi;
    else:
        hourbuffer=hi;
        miubuffer=mi;
timelist.sort(reverse=True);
print(timelist[0]);