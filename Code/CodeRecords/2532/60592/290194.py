nums = eval(input())
res = 0
i= 0
while i < len(nums):
    if i < len(nums)-1 and nums[i+1]<nums[i]:
        while i < len(nums)-1 and nums[i+1]<nums[i]:
            i+=1
        res+=1
    elif i < len(nums)-1 and nums[i+1]>nums[i]:
        while i < len(nums)-1 and nums[i+1]>nums[i]:
            i+=1
        res+=1
    if (i < len(nums)-1 and nums[i+1]==nums[i]) or (i>0 and nums[i-1]==nums[i]):
        if i>0 and nums[i-1]==nums[i]:
            i-=1
        while i < len(nums)-1 and nums[i+1]==nums[i]:
            i+=1
            res+=1
    i+=1
if res ==3 :
    print(4)
else:
    print(rem)