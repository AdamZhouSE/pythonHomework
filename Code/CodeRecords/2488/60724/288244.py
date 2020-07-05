nums=eval(input())
nums.sort()
i=1
while i<len(nums)-1:
    nums[i],nums[i+1]=nums[i+1],nums[i]
    i+=2
print(nums)