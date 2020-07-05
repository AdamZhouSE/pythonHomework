nums=list(eval(input()))
nums.sort()
for i in range(1,nums[len(nums)-1]+1):
    if i not in nums:
        print(i)
        exit()
print(nums[len(nums)-1]+1)