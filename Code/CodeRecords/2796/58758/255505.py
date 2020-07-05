import math

n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
for i in range(len(nums)-1, -1, -1):
    if nums[i] < 0:
        print(nums[i])
        break
    sq = math.sqrt(nums[i])
    if int(sq) != sq:
        print(nums[i])
        break
