nums = list(map(int, input()[1:-1].split(",")))
count = 0
result = 0
for i in range(1, len(nums)+1):
    for j in range(len(nums)):
        if nums[j] >= i:
            count += 1
        if count >= i:
            result = i
            break
    count = 0
print(result)
