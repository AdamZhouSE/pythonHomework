nums = input().split(",")
target = input()
if target in nums:
    print(nums.index(target))
else:
    print("-1")