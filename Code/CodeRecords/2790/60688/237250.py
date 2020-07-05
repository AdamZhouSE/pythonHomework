nums=(input().split(" "));
alen=int(nums[0]);
blen=int(nums[1]);
alist=input().split(" ");
alist=list(int(x) for x in alist);
alist.sort();
blist=input().split(" ");
blist=list(int(x) for x in blist);
result=[0]*blen;
for i in range(blen):
    for j in range(alen):
        if(alist[j]<=blist[i]):
            result[i]+=1;
outstr="";
for i in range(blen-1):
    outstr+=str(result[i])+" ";
outstr+=str(result[blen-1]);
print(outstr);