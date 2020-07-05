inp = input().split(',')
nums = list(map(int,inp))
temp = nums[0]
m = temp
for i in range(1,len(nums)):
    if temp+nums[i]>nums[i]:
        m = max(m,temp+nums[i])
        temp = temp+nums[i]
    else:
        m = max(m,temp,nums[i],temp+nums[i])
        temp = nums[i]
print(m)