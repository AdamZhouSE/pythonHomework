n = int(input())
nums = []
res = 0
for i in range(n):
    nums.append((int(input())))
if(n==1):
    print(0)
else:
    for i in range(1,n-1):
        if nums[i-1]<nums[i]:
            res+=nums[i]
        if(nums[i]>=nums[i+1]):
            res+=nums[i]
            
    if(nums[0]>=nums[1]):
        res+=nums[0]
    if(nums[n-2]<nums[n-1]):
        res+=nums[n-1]
print(res)