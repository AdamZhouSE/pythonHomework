nums = int(input())
list_nums = []
for i in range(nums):
    line = int(input())
    list_nums.append(line)
for i in range(nums):
    line = list_nums[i]
    print(line * (2 * line + 1))
