nums=eval(input())
nums.sort()
gap=0
for i in range(0,len(nums)-1):
    if nums[i+1]-nums[i]>gap:
        gap=nums[i+1]-nums[i]
print(gap)