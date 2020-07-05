nums = [int(i) for i in input().split(',')]
glo = 0
loc = 0
for i in range(len(nums)-1):
    if(nums[i]>nums[i+1]):loc+=1
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):glo+=1
if(loc==glo):print(True)
else:print(False)