nums=int(input());
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
numslist.insert(0,0);
power=0;
money=0;
for i in range(nums-1):
    hinow=numslist[i];
    hinext=numslist[i+1];
    power=power+hinow-hinext;
    if power<0:
        money+=-power;
        power=0;
print(money);