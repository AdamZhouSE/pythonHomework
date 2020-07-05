n=int(input())
for i in range(n):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    res={}
    
    for j in nums:
        if j not in res:
            res[j]=-1
        if j+1 in res:
            res[j+1]=j
        if j-1 in res:
            res[j]=j-1
    maxLength=1
    k=0
    while k<length:
        tempLength=1
        next=res[nums[k]]
        while next!=-1:
            tempLength+=1
            next=res[next]
        maxLength=max(maxLength,tempLength)
        k=k+1
    print(maxLength)