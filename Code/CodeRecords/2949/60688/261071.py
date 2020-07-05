numslist = (input().split(" "));
numslist=numslist[0:len(numslist)-1]
numslist.reverse();
result=" ".join(numslist)
print(result)