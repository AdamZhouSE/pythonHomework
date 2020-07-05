nums = [int(x) for x in input()[1:-1].split(",")]
target = int(input())
if target in nums:
    print(-1)
else:
    print(nums.index(target))
