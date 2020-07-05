nums = sorted(list(map(int, input()[1:-1].split(","))))
length = 1
for i in range(len(nums)-1):
    if nums[i+1] - nums[i] == 1:
        length += 1
    else:
        break
print(length)

