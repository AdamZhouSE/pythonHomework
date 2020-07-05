import math
def insertBinSearch(nums,x):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]==x: return mid
        elif nums[mid]<x: left=mid+1
        else: right=mid-1
    return (right-left)/2
def findKelem(nums,k,x):
    idx=insertBinSearch(nums,x)
    i=math.ceil(idx-1)
    j=math.ceil(idx+1)
    while i>=0 and j<len(nums) and j-i-1<k:
        right=nums[j]-x
        left=x-nums[j]
        if left<=right:
            i-=1
        elif left>right:
            j+=1
    if i<0: j=k
    if j==len(nums): i=j-k
    return nums[i+1:j]
nums=eval(input())
k=int(input())
x=int(input())
print(findKelem(nums,k,x))