numbers=int(input())
for i in range(numbers):
    brands=int(input())
    blist=input().split()
    blist=[int(x) for x in blist]
    blist.sort(reverse=True)
    res=1
    for k in range(brands):
        if blist[k]<=k+1:
            temp=blist[k]
            if res<temp:
                res=temp
    print(res)