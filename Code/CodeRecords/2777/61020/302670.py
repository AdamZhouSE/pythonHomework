import math

T = int(input())

for i in range(T):
    trash = input()
    nums = input().split()
    for j in range(len(nums)):
        nums[j] = int(nums[j])
    nums.sort()

    index = len(nums) // 2
    if len(nums) % 2 != 0:
        print(nums[len(nums) // 2])
    else:
        print(int(math.floor((nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2)))
