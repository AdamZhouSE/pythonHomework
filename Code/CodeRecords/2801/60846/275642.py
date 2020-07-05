def triangle(nums):
    for i in range(2,len(nums)):
        if nums[i-2]+nums[i-1]>nums[i]: return True
    return False
n=int(input())
nums=[int(x) for x in input().split()]
nums.sort()
if triangle(nums): print("YES")
else: print("NO")

        