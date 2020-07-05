nums = list(map(int, input()[1:-1].split(",")))
Max = 0
count = 0
for i in range(len(nums)):
    Max = max(Max, nums[i])
    if Max == i:
        count += 1
print(count)
