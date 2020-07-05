def contains(nums, i):
    for j in range(0, len(nums)):
        if nums[j] == i:
            return True
    return False


times = int(input())
for i in range(0, times):
    n = int(input())
    nums = input().split()
    for i in range(0, n):
        nums[i] = int(nums[i])
    nums.sort()
    minPositive = nums[0]
    for i in range(0, n):
        if nums[i] >= 0:
            minPositive = nums[i]
    maxPositive = nums[-1]
    for i in range(1, maxPositive + 2):
        if contains(nums, i):
            continue
        print(i)
        break