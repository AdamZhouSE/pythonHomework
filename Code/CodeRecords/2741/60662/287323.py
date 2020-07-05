nums = list(map(int, input().strip('[]').split(',')))
count = 1
m = 1
for i in range(0, len(nums) - 1):
    if nums[i] < nums[i + 1]:
        count = count + 1
    else:
        if m < count:
            m = count
        count = 1
print(m)