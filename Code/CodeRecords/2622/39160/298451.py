nums = list(eval(input()))

count, majority = 1, nums[0]
for num in nums[1:]:
    if count == 0:
        majority = num
    if num == majority:
        count += 1
    else:
        count -= 1
print(majority)
 