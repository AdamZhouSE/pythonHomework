from itertools import combinations
nums = input().split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
l = [list(x) for x in list(combinations(range(1, 10), nums[0])) if sum(x) == nums[1]]
print(l)