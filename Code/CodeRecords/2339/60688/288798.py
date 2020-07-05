times=int(input())
for a in range(0,times):
    n=int(input())
    numslist=input().split(" ")
    numslist=list(int(b) for b in numslist)
    res=0
    for c in range(0,n):
        for d in range(c+1,n):
            if(numslist[c]>numslist[d]):
                res=res+1
    print(res)
    