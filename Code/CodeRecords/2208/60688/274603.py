times=int(input());
#首先是单次的
results=[];
for j in range(times):
    nums=int(input());
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    result=[-1];
    for i in range(1,nums):
        previewnum=numslist[i-1];
        if(numslist[i]>previewnum):
            result.append(previewnum);
        else:result.append(-1);
    result=list(str(x) for x in result);
    result=" ".join(result);
    results.append(result);
for i in results:
    print(i)