n=int(input())
nums=[int(x) for x in input().split()]
nums.sort()
import math
for i in range(len(nums)-1,-1,-1):
    if nums[i]>=0:
        j= math.sqrt(nums[i])
        if int(j)!=j:
            print(nums[i])
            break
    else:
        print(nums[i])
        break