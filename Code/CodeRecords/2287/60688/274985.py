times=int(input());
results=[];
for j in range(times):
    nums=int(input());
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    result=[];
    for i in range(0,nums-1):
        thisnum=numslist[i];
        flagthis=False;
        for j in range(i+1,nums):
            if(numslist[j]>thisnum):
                flagthis=True;
                result.append(numslist[j])
                break;
            else:continue;
        if(flagthis==False):
            result.append(-1);
    result.append(-1);
    result=list(str(x) for x in result);
    result=" ".join(result);
    results.append(result);
for i in results:
    print(i);