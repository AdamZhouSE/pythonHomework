nums = [int(x) for x in input()[1:-1].split(",")]
target = int(input())
print(nums, target)
if target in nums:
    print(nums.index(target))
else:
    print(-1)
