nums=input().split(',')
nums=[int(x) for x in nums]
n=len(nums)-1
if len(nums)==3:
    print(nums[0]*nums[1]*nums[2])
    exit()
nums.sort()
if nums[1]>=0:
    print(nums[n]*nums[n-1]*nums[n-2])
else:
    print(max(nums[n]*nums[0]*nums[1],nums[n]*nums[n-1]*nums[n-2]))