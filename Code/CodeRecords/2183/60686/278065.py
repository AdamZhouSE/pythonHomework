nums = int(input())
list_nums = []
for i in range(nums):
    line = int(input())
    list_nums.append(line)
for i in range(nums):
    line = list_nums[i]
    maximum = line * line + line
    sum = 0
    for j in range(maximum, maximum - line * 2, -1):
        sum += j
    print(sum)
