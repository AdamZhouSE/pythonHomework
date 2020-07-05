numbers=int(input())
for i in range(numbers):
    brands=int(input())
    blist=input().split()
    j=0
    for j in range(len(blist)):
        blist[j]=int(blist[j])
    blist.sort(reverse=True)
    res=1
    k=0
    for k in range(brands):
        if blist[k]>=k+1:
            temp=min(blist[k],k+1)
            if res<temp:
                res=temp
    print(res)