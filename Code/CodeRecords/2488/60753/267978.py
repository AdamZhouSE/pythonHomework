import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=len(nums)
if n<=2:
    nums.sort()
    print(nums)
else:
    for i in range(1,n-1):
        if nums[i]<=nums[i-1] and nums[i]>nums[i+1]:
            swap=nums[i]
            nums[i]=nums[i-1]
            nums[i-1]=swap
        elif nums[i]>=nums[i-1] and nums[i]<nums[i+1]:
            swap=nums[i]
            nums[i]=nums[i+1]
            nums[i+1]=swap
        else:
            pass
    print(nums)
   