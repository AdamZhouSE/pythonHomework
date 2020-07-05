import math
n=int(input())
nums=input().split(' ')
nums=[int(x) for x in nums]
res=-999
for i in range(n):
    if nums[i]<0 or(nums[i]!=0 and math.sqrt(nums[i])%1!=0):
        res=max(nums[i],res)
print(res)