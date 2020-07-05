def mincosttime(arr):
    insum=arr[0];
    exsum=0;
    for i in range(1,len(arr)):
        thisinsum=min(exsum,insum)+arr[i]
        thisexsum=insum;
        insum=thisinsum
        exsum=thisexsum
    return min(insum,exsum)
nums=int(input())
results=[];
for i in range(nums):
    times=input();
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    tempresult=mincosttime(numslist)
    results.append(tempresult)
for i in results:
    print(i)