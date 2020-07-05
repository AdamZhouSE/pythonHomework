nums = list(map(int, input().split(",")))
target = int(input())
if not target in nums:
    print(-1)
else:
    print(nums.index(target))
