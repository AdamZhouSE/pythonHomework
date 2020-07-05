numslist=(input().split(" "));
n=int(numslist[0]);
carry=int(numslist[1]);
numslist=(input().split(" "));
numslist=list(int(x) for x in numslist);
times=0;
for i in range(n-1):
    if numslist[i]<numslist[i+1]:
        continue;
    while numslist[i]>=numslist[i+1]:
        numslist[i+1]+=carry;
        times+=1;
print(times);