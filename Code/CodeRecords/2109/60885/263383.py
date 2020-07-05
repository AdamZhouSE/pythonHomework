nums = list(map(int, list(input())))
while len(nums) > 1:
    total = 0
    for num in nums:
        total += num
    nums = list(map(int, list(str(total))))
print(nums[0])