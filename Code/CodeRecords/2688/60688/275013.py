
def issubsum(numlist,n,sum):
    if(sum==0):
        return 1;
    if(n==0 and sum!=0):return 0;
    if(numlist[n-1]>sum):
        return issubsum(numlist,n-1,sum);
    return issubsum(numlist,n-1,sum) +issubsum(numlist,n-1,sum-numlist[n-1])
times=int(input());
results=[];
for j in range(times):
    nums=int(input());
    numslist = (input().split(" "));
    sum=int(input());
    numslist=list(int(x) for x in numslist);
    result=issubsum(numslist,nums,sum);
    results.append(str(result));
for i in results:
    print(i);