nums=input().split(",")
for o in range(len(nums)):
    nums[o]=int(nums[o])
lower=int(input())
upper=int(input())
count=0
sum=0
for i in range(len(nums)):
    if nums[i]>=lower and nums[i]<=upper:
        count+=1
for j in range(len(nums)):
    k=j+1
    while k<len(nums):
        for p in range(j,k+1):
            sum = sum + nums[p]
        if sum>=lower and sum<=upper:
            count+=1
        sum=0
        k=k+1
print(count)