numslist=(input().split(" "));
lines=int(numslist[0]);
allnums=int(numslist[1]);
resultset=[];
for i in range(lines):
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    for j in range(1,numslist[0]+1):
        resultset.append(numslist[j]);
resultset=set(resultset);
if(len(resultset)==allnums):
    print("YES");
else:print("NO");