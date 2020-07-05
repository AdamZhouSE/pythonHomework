nums=int(input())
results=[];
for i in range(nums):
    times=int(input());
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    temp=0;
    for j in range(times-1):
        for k in range(j+1,times):
            if numslist[j]==numslist[k]:
                temp+=1;
    results.append(temp)
for i in results:
    print(i)