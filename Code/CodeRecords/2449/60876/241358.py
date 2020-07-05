import sys
nums=sys.stdin.readline().split(",")
target=sys.stdin.readline()
if target in nums:
    print(nums.index(target))
else:
    print(-1)
