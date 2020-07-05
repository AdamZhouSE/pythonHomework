nums=int(input());
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
inqnums=int(input());
inqlist = (input().split(" "));
inqlist=list(int(x) for x in inqlist);
bookbegs=[1];
sums=0;
for i in numslist:
    sums+=i;
    bookbegs.append(sums+1);
bookbegs=bookbegs[0:nums];
#print(bookbegs)
#print(inqlist)
for inq in inqlist:
    for i in range(nums-1):
        if inq>=bookbegs[i] and inq<bookbegs[i+1]:
            print(i+1);
            break;
        if i==nums-2:
            print(nums)