import math

nums = [int(i) for i in input().split(',')]
nums.sort()
out = 0
while(len(nums)>0):
    out+=math.ceil(nums.count(nums[0])/(nums[0]+1))*(nums[0]+1)
    nums=nums[nums.count(nums[0]):]

print(out)