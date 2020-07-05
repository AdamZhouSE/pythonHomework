nums = input().split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

flag = False

for i in range(0, len(nums) - 1):
    if nums[i] > nums[i + 1]:
        index = i
        flag = True
        break

if flag:
    print(index)
else:
    print(len(nums) - 1)