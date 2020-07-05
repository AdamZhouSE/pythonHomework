def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
nums=int(input())
results=[];
for i in range(nums):
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    l=numslist[1]-1
    r=numslist[2]
    twostrtarg=list(toStr(numslist[0],2));
    twostrtarg.reverse();
    tempstr="".join(twostrtarg[l:r])
    templists=twostrtarg[0:l];
    templists.extend(twostrtarg[r:])
    # for i in range(l,r):
    #     twostrtarg.pop(i)
    tempstr=tempstr.replace("0","1")
    templists.insert(l,tempstr);
    templists.reverse();
    numresult=int("".join(templists),2);
    results.append(numresult);
for i in results:
    print(i)