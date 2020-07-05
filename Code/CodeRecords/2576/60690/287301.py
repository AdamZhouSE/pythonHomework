nums=input().split(",")
for i in range(len(nums)):nums[i]=int(nums[i])
target=int(input())
nums.sort()

sum=0
for e in nums:sum+=e

res=0
if sum<=target: res=max(nums)
else:
    res=target/len(nums)
    if round(res)>res:
        little=int(res)
        suml,sumb=0,0
        for e in nums:
            if e>little: suml+=little
            else: suml+=e
            if e>round(res): sumb+=round(res)
            else: sumb+=e
            if abs(suml-target)==abs(sumb-target):
                res=little
            else:
                res=round(res)
    res=round(res)       
    
print(res)