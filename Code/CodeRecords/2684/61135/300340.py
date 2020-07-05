def mintime(arr):
    insum=arr[0]
    exsum=0
    for i in range(1,len(arr)):
        thisinsum=min(exsum,insum)+arr[i]
        thisexsum=insum
        insum=thisinsum
        exsum=thisexsum
    return min(insum,exsum)
T=int(input())
results=[]
for i in range(T):
    times=input()
    numslist = (input().split(" "))
    numslist=list(int(x) for x in numslist)
    mid=mintime(numslist)
    results.append(mid)
for i in results:
    print(i)