nums=input()[1:-1].split(",")
nums=list(map(int,nums))
res=dict()
maxNum=1
for i in nums:
    if i not in res:
        if i-1 in res:
            res[i-1]=i
            res[i]=-1
        if i+1 in res:
            res[i]=i+1
        else:
            res[i]=-1
for i in range(len(nums)):
    next=res[nums[i]]
    if next==-1:
        continue
    length=1
    while res[next]!=-1:
        length=length+1
        next=res[next]
    length=length+1
    maxNum=max(length,maxNum)
print(maxNum)