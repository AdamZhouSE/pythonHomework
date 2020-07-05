nums = input().split(',')
nums = list(map(int, nums))
sum_set_nums = sum(set(nums))
res = [sum(nums) - sum_set_nums, len(nums) * (len(nums) + 1) // 2 - sum_set_nums]
print(res)