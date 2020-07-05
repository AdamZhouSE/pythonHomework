nums = eval(input())
n = len(nums)
for i in range(n-1):
    if(i%2==0 and nums[i]>=nums[i+1]):
        temp =nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp
    if(i%2==1 and nums[i]<=nums[i+1]):
        temp =nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp
print(nums)