nums = [int(i) for i in input().split(',')]
the_sum = 0
min_value = nums[0]
for i in nums:
    if i < min_value:
        min_value = i
    the_sum += i
print(the_sum - min_value * len(nums))
