nums = [int(x) for x in input().split(',')]
n = len(nums)
for i in range(1, n):
    if nums[i - 1] > nums[i] and nums[i - 1] - nums[i] > 1:
        print(False)
        exit()
print(True)