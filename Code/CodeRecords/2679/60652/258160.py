def count(n,bCount,cCount):
    if bCount<0 or cCount<0:
        return 0
    if n==0:
        return 1
    if bCount==0 and cCount==0:
        return 1
    res=count(n-1,bCount,cCount)
    res+=count(n-1,bCount-1,cCount)
    res+=count(n-1,bCount,cCount-1)
    return res

T=int(input())
for i in range(0,T):
    n=int(input())
    c=count(n,1,2)
    print(c)