nums=int(input());
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
num=0;
for i in range(nums-1):
    if (i%2==0):
        num=max(numslist);#!!
    else:num=min(numslist);
    numslist.remove(num);
    # index=numslist.index(num);

print(numslist[0]);