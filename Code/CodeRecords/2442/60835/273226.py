nums = eval(input())
nums.sort()
result = 0
if len(nums) < 2:
    pass
else:
    for n in range(len(nums) - 1):
        tem = nums[n + 1] - nums[n]
        if tem > result:
            result = tem
print(result)