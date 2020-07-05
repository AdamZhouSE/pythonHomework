nums = sorted(list(map(int, input().split(","))))
result = []
for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 0:
        result.append(nums[i+1])
    if nums[i+1] - nums[i] == 2:
        result.append(nums[i+1]-1)
if nums[0] != 1:
    result.append(1)
print(result)
