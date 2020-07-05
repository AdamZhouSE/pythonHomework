def findMaxSum(inq:[[int]],arr:[int],n):
    visitTimes=[0 for _ in range(n)]
    for l,r in inq:
        if l==r:
            visitTimes[l-1]+=1
        else:
            for i in range(l-1,r):
                visitTimes[i]+=1
    visitTimes.sort()
    arr.sort()
    res=0
    for i in range(n):
        res+=visitTimes[i]*arr[i]
    return res

nq=input().split()
n,q=int(nq[0]),int(nq[1])
arr=list(map(int,input().split()))
inq=[]
for _ in range(q):
    lr=list(map(int,input().split()))
    inq.append(lr)

print(findMaxSum(inq,arr,n))
