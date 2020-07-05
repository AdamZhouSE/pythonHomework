times=int(input());
#首先是单次的
results=[];
for j in range(times):
    nums=int(input());
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    result=[-1];
    if(numslist[0]<numslist[1]):
        result.append(numslist[0]);
    else:result.append(-1);
    for i in range(2,nums):
        flag=True;
        for j in range(i-1,-1,-1):
            if(numslist[j]<numslist[i]):
                result.append(numslist[j]);
                flag=False;
                break;
        if flag:
            result.append(-1);
    result=list(str(x) for x in result);
    result=" ".join(result);
    results.append(result);
for i in results:
    print(i,end=" ");
    print()
print('\n')