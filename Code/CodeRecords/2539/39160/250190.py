import sys, os, io

nums = eval(input())

nums_copy=nums[:]
nums_copy.sort()
left=float("inf")
right=0
for i in range(len(nums)):
    if(nums_copy[i]!=nums[i]):
        left=min(left,i)
        right=max(right,i)
        
result = right-left+1 if(right-left+1 > 0) else 0

print(result)