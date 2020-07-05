def goodTogo(nums, min):
    for i in nums:
        if i % min != 0:
            return False
    return True

n = int(input())
nums = input().split()
for i in range(0, n):
    nums[i] = int(nums[i])
min = nums[0]
for i in range(0, n):
    if nums[i] < min:
        min = nums[i]
count = 0
for i in range(1, min + 1):
    if goodTogo(nums, i):
        count += 1
print(count)