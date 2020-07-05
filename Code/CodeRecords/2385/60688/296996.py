import math
print(math.ceil(3/2))
times=int(input());
allresults=[];
for _ in range(times):
    n=int(input());
    result=[];
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    while(numslist!=[-1]*n):
        maxindex=0;
        minindex=0;
        for i in range(len(numslist)):
            if(numslist[i]==-1 ):
                continue;
            else:
                maxindex=minindex=i;
                break;
        for i in range(len(numslist)):
            if(numslist[i]>numslist[maxindex] and numslist[i]!=-1):
                maxindex=i;
            if(numslist[i]<numslist[minindex] and numslist[i]!=-1):
                minindex=i;
        max=str(numslist[maxindex]);
        min=str(numslist[minindex]);
        numslist[maxindex]=-1;
        numslist[minindex]=-1;
        result.append(max)
        if maxindex!=minindex:
            result.append(min);
    allresults.append(" ".join(result));
print(allresults)