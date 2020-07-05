nums=eval(input())
target=eval(input())
if not target in nums:
    print(-1)
else:
    print(nums.index(target))