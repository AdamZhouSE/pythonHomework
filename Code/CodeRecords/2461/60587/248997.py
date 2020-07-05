nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
# print(num)


# res = 0
# if nums[len(nums) - 1] < nums[len(nums) - 2]:
#     res = len(nums) - 1
# for i in range(1, len(nums) - 1):
#     if (nums[i] < nums[i - 1]) & (nums[i] < nums[i + 1]):
#         res = i
#         break
# print(nums[res])


lst = list(num)
lst.sort()
print(lst[0])