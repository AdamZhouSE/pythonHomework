reqlist = (input().split(" "));
reqlist=list(int(x) for x in reqlist);
numslist = (input().split(" "));
numslist=list(int(x) for x in numslist);
for i in range(reqlist[1]):
    specreq = (input().split(" "));
    specreq=list(int(x) for x in specreq);
    lindex=specreq[1];
    rindex=specreq[2];
    if(specreq[0]==0):
        templist=sorted(numslist[lindex-1:rindex],reverse=False);
        numslist=numslist[0:lindex-1]+templist+numslist[rindex:]
    else:
        templist=sorted(numslist[lindex-1:rindex],reverse=True);
        numslist=numslist[0:lindex-1]+templist+numslist[rindex:]
treindex=int(input())
print(numslist[treindex-1])