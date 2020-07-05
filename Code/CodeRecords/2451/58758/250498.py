nums = [int(x) for x in input().split(',')]
target = int(input())
i = 0
while i < len(nums) and nums[i] < target:
    i += 1
print(i)
