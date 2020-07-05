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
first="".join(finalnums);
secondlist=list(first);
secondlist=list([int(x)for x in secondlist]);
res="";
#处理从N个数中取出N-M个数，为max，原顺序不变，RQM算法思想：：
l=0;r=delnums+1;
allnums=len(first)-delnums;
while (allnums!=0 and r<=len(secondlist)):
    tempmax=max(secondlist[l:r]);
    pos=secondlist[l:r].index(tempmax);
    res+=str(tempmax);
    l=pos+1;
    r+=1;
    allnums-=1;

print(first)
print(res)