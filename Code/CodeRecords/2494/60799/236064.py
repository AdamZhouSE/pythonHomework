nums = [int(i) for i in input().strip('[|]').split(',')]
res = [(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] > 2 * nums[j]]
print(len(res))