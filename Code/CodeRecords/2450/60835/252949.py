nums = input().split(',')
target = input()
result = [-1, -1]

if target in nums:
    result[0] = nums.index(target)
nums.reverse()

if target in nums:
    result[1] = len(nums) - nums.index(target) - 1
print(result)