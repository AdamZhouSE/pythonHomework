nums=sorted(eval(input()))
max=0
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]>max:
        max=nums[i]-nums[i-1]
print(max)