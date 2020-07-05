nums=int(input());
results=[];
for i in range(nums):
    numslist = (input().split(" "));
    indes=int(input());
    numslist=list(int(x) for x in numslist);
    diff=numslist[1]-numslist[0];
    for j in range(2,indes):
        temp=numslist[j-1]+diff;
        numslist.append(temp)
    results.append(numslist[indes-1])
for i in results:
    print(i)