t=int(input())
res=[]
for i in range(t):
    list=input().split(" ")
    n=int(list[0])
    m=int(list[1])
    l=int(list[2])
    r=int(list[3])
    nums=input().split(" ")
    for j in range(len(nums)):
        if nums[j]=='':nums.pop(j)
        else:nums[j]=int(nums[j])

    count=[]
    for j in range(max(max(nums),r)+1):count.append(0)
    for e in nums:count[e]+=1

    while sum(count)<n+m:
        isAdd=False
        for e in range(l,r+1):
            if count[e]==0:
                count[e]=1
                isAdd=True
        if isAdd==False:
            index=l
            minmun=count[index]
            for j in range(l,r+1):
                if count[j]<minmun:
                    index=j
                elif minmun==-1:
                    minmun=count[j]
                    index=j
            count[index]+=1


    thisres=1
    for j in range(n+m):
        thisres*=j+1
    for e in count:
        if e>1:
            for j in range(e):
                thisres=int(thisres/(j+1))
    res.append(thisres)
for e in res:print(e%998244353)