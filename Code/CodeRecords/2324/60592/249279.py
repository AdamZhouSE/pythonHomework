nums = list(map(int,input().split(',')))
k = int(input())
nums.sort()
for i in range(1,len(nums)):
    if nums[i]-nums[0]>=k:
        nums[i]-=k
    else:
        nums[i]+=k
nums[0]+=k
nums.sort()
print(nums[len(nums)-1]-nums[0])