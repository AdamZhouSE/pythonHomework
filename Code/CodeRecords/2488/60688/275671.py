numslist:list=eval(input());
totallen=len(numslist);
numslist.sort();
minnumlistlen=int(totallen/2)
if minnumlistlen*2!=totallen:
    minnumlistlen+=1;
maxnumlistlen=totallen-minnumlistlen;
minnums=numslist[0:minnumlistlen];
minnums.reverse();
maxnums=numslist[minnumlistlen:totallen];
maxnums.reverse();

# print(minnums)
# print(maxnums)
result=[];
minindex=0;
maxindex=0;
allindex=0;
while(allindex<totallen):
    if allindex%2==0:
        result.append(minnums[minindex]);
        allindex+=1;
        minindex+=1;
    else:
        result.append( maxnums[maxindex]);
        allindex += 1;
        maxindex += 1;

print(result)