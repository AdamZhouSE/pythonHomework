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

#处理从N个数中取出N-M个数，为max，原顺序不变，贪心算法：：总是从前向后扫描并删除l<r 中的l并且操作一次重新迭代！！
allnums=delnums;
while (allnums!=0):
    for i in range(len(secondlist)-1):
        if secondlist[i]<secondlist[i+1]:
            secondlist.pop(i);
            allnums-=1;
            break
secondlist=[str(x)for x in secondlist];
res="".join(secondlist)

print(first)
print(res,end="")