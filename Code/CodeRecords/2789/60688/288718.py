times=int(input())
for a in range(0,times):
    numslist=int(input())
    l=input().split(" ")
    l=list(int(a) for a in l)
    l=sorted(l)
    max=l[-1]
    while(max>0):
        count=0
        for b in range(1,max+1):
            if(numslist-b>=0 and l[numslist-b]>=max):
                count=count+1
        if(count==max):
            print(max)
            break
        else:
            max=max-1