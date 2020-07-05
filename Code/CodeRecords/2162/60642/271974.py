nums = [int(i) for i in input().split()]
out = 1
for i in range(nums[1]):
    out=out*nums[0]
print(out)