nums = list(map(int, input()[1:-1].split(",")))
i = 0
count = 0
temp = 1
while i < len(nums)-1:
    if nums[i] < nums[i+1]:
        temp += 1
    else:
        count = max(count, temp)
        temp = 1
    i += 1
print(count)
