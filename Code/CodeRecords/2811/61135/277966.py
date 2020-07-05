inp=input();
numsline=inp.split(" ");
res=-1;
allnums=int(numsline[0]);
num=int(numsline[1]);
list=[-1]*allnums;
i=0;
while i<num:
    tep=int(input());
    index=tep%allnums;
    if(list[index]==-1):
        list[index]=tep;
    else:
        res=i+1;
        break;
    i = i + 1;
print(res);