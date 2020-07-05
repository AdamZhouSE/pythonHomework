numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
times=numslist[0];
delnums=numslist[1];
mynumlist=[1];
finalnums=[];
for i in range(times):
    num=mynumlist.pop(0);
    mynumlist.append(2*num+1)
    mynumlist.append(4*num+5)
    finalnums.append(num);
finalnums.extend(mynumlist)
finalnums=sorted(finalnums);
finalnums=finalnums[0:times]
finalnums=list(str(x) for x in finalnums);
first=" ".join(finalnums);
secondlist=finalnums[delnums-1:]
second=" ".join(secondlist)
print(delnums)
print(first)
print(second)