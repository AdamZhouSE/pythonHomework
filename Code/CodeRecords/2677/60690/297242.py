t=int(input())
res=[]
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for j in range(len(nums)):
        nums[j]=int(nums[j])
    this=0
    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[j]==nums[k]:
                this+=1
    res.append(this)
for e in res:print(e)